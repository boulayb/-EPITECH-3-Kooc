from pyrser.grammar import Grammar
from pyrser import meta
from cnorm.parsing.declaration import Declaration
from cnorm import nodes
import copy
import kooc_mangling
import kooc_implementation
import kooc_utils
import kooc_typage


class KoocData:
    def __init__(self):
        self.importList = []
        self.modulesList = {}
        self.typeList = {}

    def __repr__(self):
        return "Import List : " + str(self.importList) + "  Module List : " + str(self.modulesList)


class Kooc(Grammar, Declaration):
    def __init__(self, path=""):
        super(Kooc, self).__init__()
        self.srcpath = "./" + path
        self.koocdata = KoocData()

    entry = 'init'

    grammar = """

    init =
    [
      translation_unit:>_
    ]

    declaration =
    [
      Declaration.declaration:>_
      | kooc_decl

    ]

    kooc_decl =
    [
      kooc_import
      | kooc_module
      | kooc_class
      | kooc_implementation
    ]

    kooc_import =
    [
      "@import" Base.string:importFile
      #add_import(importFile, current_block)
    ]

    kooc_module =
    [
      "@module" Base.id:moduleName
      #add_module(moduleName)
      '{'
         [ c_decl #add_module_content(moduleName, current_block) ]*
      '}'
    ]

    kooc_class =
    [
      "@class" Base.id:className [ ':' Base.id ]?
      '{'
      #add_class(className)
         [
           c_decl
           | kooc_member
           | kooc_virtual
         ]*
      '}'
    ]

    kooc_implementation =
    [
      __scope__:scope_implementation
      "@implementation" Base.id:name
      '{'
      #add_implementation(name, scope_implementation, current_block)
         [
           c_decl #simple_implementation(name, current_block)
           | kooc_member
           | kooc_virtual
         ]*
      '}'
    ]

    kooc_member =
    [
      "@member"
      [
        '{'
            [
              c_decl #member_implementation(scope_implementation, current_block)
              | kooc_virtual
            ]*
        '}'
      ]
      |
      [ c_decl #member_implementation(scope_implementation, current_block) ]

    ]

    // Bloquer les decl de variable
    // Faire le check dans un hook ( -> returner false)
    kooc_virtual =
    [
      "@virtual"
      [
        '{'
           [
             c_decl #virtual_implementation(scope_implementation, current_block)
           ]*
        '}'
      ]
      // manquerait pas un "| c_decl" ici ?
    ]

    primary_expression =
    [
      kooc_call:>_
      | Declaration.primary_expression:>_

    ]

    kooc_call =
    [
      [ specific_kooc_call:>_
      | generic_kooc_call:>_ ]
    ]

    specific_kooc_call =
    [
      "@!" '(' type_name:t ')'
      '[' Base.id:modulename
        [
          [ Base.id:funcname specific_list_parametre:params #specific_kooc_call_func(_, t, modulename, funcname, params) ]
          | @ignore("null") module_variable:varname #specific_kooc_call_var(_, t, modulename, varname)
        ]
      ']'
    ]

    specific_list_parametre =
    [
      #is_specific_list_parametre(_)
      [ ':' '(' type_name:t ')' Expression.assignement_expression:param #add_specific_list_parametre(_, t, param)]*
    ]

    generic_kooc_call =
    [
      '['
        [
          generic_kooc_call_func:>_
          | generic_kooc_call_var:>_
        ]
      ']'
    ]

    generic_kooc_call_func =
    [
        [Base.id Base.id]:func_name generic_list_parametre:params  #generic_kooc_call_func(_, func_name, params)
    ]

    generic_kooc_call_var =
    [
        @ignore("null")
        [ Base.id module_variable ]:var #generic_kooc_call_var(_, var)
    ]

    generic_list_parametre =
    [
      #is_generic_list_parametre(_)
      [ ':' Expression.assignement_expression:param #add_generic_list_parametre(_, param) ]*
    ]

    module_variable =
    [
      '.' id:variable_name
      #is_module_variable(_, variable_name)
    ]

    """


@meta.hook(Kooc)
def add_import(self, filename, current_block):
    from kooc_import import KoocImport
    raw_file_name = self.value(filename)[1:-1]
    if raw_file_name not in self.koocdata.importList:
        self.koocdata.importList.append(raw_file_name)
        current_block.ref.body.append(KoocImport(raw_file_name, self.srcpath[:self.srcpath.rfind("/")], self.koocdata))
    return True


@meta.hook(Kooc)
def add_module(self, modulename):
    if self.value(modulename) == "_":
        raise Exception("_ : not a valid module name")
    if self.value(modulename) not in self.koocdata.modulesList:
        self.koocdata.modulesList[self.value(modulename)] = {'var': {}, 'func': {}, 'init var': {}}
        self.koocdata.typeList[self.value(modulename)] = {}
    return True


@meta.hook(Kooc)
def add_module_content(self, raw_modulename, current_block):
    last_decl = current_block.ref.body[-1]
    if kooc_utils.is_typedef(last_decl) or kooc_utils.is_composed(last_decl):
        return True
    modulename = self.value(raw_modulename)
    origname = last_decl._name
    kooc_mangling.mangleAttr(last_decl, modulename)
    if kooc_utils.is_init(last_decl): # INIT
        if origname not in self.koocdata.modulesList[modulename]['init var']:
            self.koocdata.modulesList[modulename]['init var'][origname] = {}
            self.koocdata.typeList[modulename][origname] = {}
        self.koocdata.typeList[modulename][origname][last_decl._name] = [kooc_utils.get_ctype(last_decl)]
        self.koocdata.modulesList[modulename]['init var'][origname][last_decl._name] = [kooc_utils.get_ctype(last_decl), copy.copy(last_decl), kooc_utils.get_value(last_decl)]
        delattr(last_decl, "_assign_expr")
        last_decl._ctype._storage = nodes.Storages.EXTERN
    elif kooc_utils.is_func(last_decl): # FUNC
        if origname not in self.koocdata.modulesList[modulename]['func']:
            self.koocdata.modulesList[modulename]['func'][origname] = {}
            self.koocdata.typeList[modulename][origname] = {}
        self.koocdata.typeList[modulename][origname][last_decl._name] = []
        self.koocdata.modulesList[modulename]['func'][origname][last_decl._name] = []
        for param in last_decl._ctype._params:
            self.koocdata.typeList[modulename][origname][last_decl._name].append(kooc_utils.get_ctype(param))
            self.koocdata.modulesList[modulename]['func'][origname][last_decl._name].append(kooc_utils.get_ctype(param))
        self.koocdata.typeList[modulename][origname][last_decl._name].append(kooc_utils.get_ctype(last_decl))
        self.koocdata.modulesList[modulename]['func'][origname][last_decl._name].append(kooc_utils.get_ctype(last_decl))
    elif kooc_utils.is_var(last_decl): # VAR
        if origname not in self.koocdata.modulesList[modulename]['var']:
            self.koocdata.modulesList[modulename]['var'][origname] = {}
            self.koocdata.typeList[modulename][origname] = {}
        self.koocdata.modulesList[modulename]['var'][origname][last_decl._name] = [kooc_utils.get_ctype(last_decl), copy.copy(last_decl)]
        self.koocdata.typeList[modulename][origname][last_decl._name] = [kooc_utils.get_ctype(last_decl)]
        last_decl._ctype._storage = nodes.Storages.EXTERN
    else:
        return False
    return True


@meta.hook(Kooc)
def add_class(self, raw_classname):
    return True


@meta.hook(Kooc)
def add_implementation(self, raw_name, scope, current_block):
    name = self.value(raw_name)
    if name in self.koocdata.modulesList:
        kooc_implementation.module_implementation(self.koocdata.modulesList[name], current_block)
    else:
        raise Exception(name + " not a declared module or class")
    scope.importname = name
    return True


@meta.hook(Kooc)
def simple_implementation(self, modulename, current_block):
    last_decl = current_block.ref.body[-1]
    if kooc_utils.is_typedef(last_decl) or kooc_utils.is_composed(last_decl):
        return True
    kooc_mangling.mangleAttr(last_decl, self.value(modulename))
    return True


@meta.hook(Kooc)
def member_implementation(self, scope, current_block):
    return True


@meta.hook(Kooc)
def virtual_implemtation(self, scope, current_block):
    return True


@meta.hook(Kooc)
def specific_kooc_call_var(self, ast, raw_type, raw_modulename, node_varname):
    modulename = self.value(raw_modulename)
    varname = node_varname.varname
    typename = self.value(raw_type)
    if modulename not in self.koocdata.modulesList:
        raise Exception(modulename + " : unknown module name")
    if varname in self.koocdata.modulesList[modulename]['var']:
        for k, v in self.koocdata.modulesList[modulename]['var'][varname].items():
            if v[0] == typename:
                ast.set(nodes.Id(k))
                return True
    if varname in self.koocdata.modulesList[modulename]['init var']:
        for k, v in self.koocdata.modulesList[modulename]['init var'][varname].items():
            if v[0] == typename:
                ast.set(nodes.Id(k))
                return True
    else:
        raise Exception(varname + " : no such variable in module " + modulename)
    raise Exception(varname + " : no version of type " + typename + " in " + modulename)


@meta.hook(Kooc)
def specific_kooc_call_func(self, ast, raw_return_type, raw_modulename, raw_funcname, params):
    modulename = self.value(raw_modulename)
    funcname = self.value(raw_funcname)
    params.paramlist[0].append(self.value(raw_return_type))
    if modulename not in self.koocdata.modulesList:
        raise Exception(modulename + " : unknown module name")
    elif funcname not in self.koocdata.modulesList[modulename]['func']:
        raise Exception(funcname + " : no such function in module " + modulename)
    for mangledname in self.koocdata.modulesList[modulename]['func'][funcname]:
        if len(self.koocdata.modulesList[modulename]['func'][funcname][mangledname]) == len(params.paramlist[0]):

            size = 0
            for idx, paramType in enumerate(self.koocdata.modulesList[modulename]['func'][funcname][mangledname]):
                if paramType != params.paramlist[0][idx]:
                    break
                size += 1
            if size == len(params.paramlist[0]):
                ast.set(nodes.Func(nodes.Id(mangledname), params.paramlist[1]))
                return True

    return True


@meta.hook(Kooc)
def is_specific_list_parametre(self, ast):
    ast.paramlist = ([], [])
    return True


@meta.hook(Kooc)
def add_specific_list_parametre(self, ast, raw_typename, value):
    ast.paramlist[0].append(self.value(raw_typename))
    ast.paramlist[1].append(value)
    return True


@meta.hook(Kooc)
def generic_kooc_call_func(self, ast, funcname, params):
    ast.set(nodes.Func(nodes.Id(funcname), params))
    return True


@meta.hook(Kooc)
def generic_kooc_call_var(self, ast, var):
    ast.set(nodes.Id(self.value(var)))
    return True


@meta.hook(Kooc)
def is_generic_list_parametre(self, ast):
    ast.paramlist = []
    return True


@meta.hook(Kooc)
def add_generic_list_parametre(self, ast, param):
    ast.paramlist.append(param)
    return True


@meta.hook(Kooc)
def is_module_variable(self, ast, varname):
    ast.varname = self.value(varname)
    return True
