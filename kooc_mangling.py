from pyrser.grammar import Grammar
from pyrser import meta
from cnorm.parsing.declaration import Declaration

from cnorm.passes import to_c

types = {
    'int' : [["i", "l", "j", "s"], ["I", "S", "L", "J"]],
    "char" : [["c", "c", "c", "c"], ["C", "C", "C", "C"]],
    "void" : [["v", "v", "v", "v"], ["v", "v", "v", "v"]],
    "float" : [["f", "f", "f", "f"], ["f", "f", "f", "f"]],
    "double" : [["d", "d", "d", "d"], ["d", "d", "d", "d"]],
}

composed = ['T', 'U', 'E']
composed_name = ['struct', 'union', 'enum']

def get_name(node):
    return str(len(node._name)) + node._name

def get_type(node, ctype):
    string = ""
    ctype_val = 'P'
    if ctype:
        ctype_val = '*'
    if ((node._ctype._decltype.__class__.__name__ == "PointerType" or \
         node._ctype._decltype.__class__.__name__ == "ArrayType") or \
        (node._ctype._decltype.__class__.__name__ == "QualType" and \
         (node._ctype._decltype._decltype.__class__.__name__ == "PointerType" or \
          node._ctype._decltype._decltype.__class__.__name__ == "ArrayType"))):
        string += get_pointer(node._ctype, ctype_val, ctype_val)
    if node._ctype._specifier is 0 or \
       (node._ctype._specifier <= 6 and \
        node._ctype._specifier >= 4):
        if ctype:
            star = string
            string = node._ctype._identifier
            if len(star) > 0:
                string += " " + star
        else :
            if node._ctype._identifier in types:
                string += str(types[node._ctype._identifier][get_sign(node)][get_specifier(node)])
            else:
                string += str(len(node._ctype._identifier)) + node._ctype._identifier
    elif node._ctype.__class__.__name__ == "ComposedType" or \
        (node._ctype._specifier >= 1 and \
         node._ctype._specifier <= 3) :
        if ctype is not True:
            string += composed[get_specifier(node)]
            if (len(node._ctype._identifier) > 0):
                string += str(len(node._ctype._identifier)) + node._ctype._identifier
        else :
            string += composed_name[get_specifier(node)]
            if (len(node._ctype._identifier) > 0):
                string += " " + node._ctype._identifier
    return (string)

def get_params(node):
    string = "_"
    if (hasattr(node._ctype, '_params')):
        node = node._ctype._params
    else :
        return ("")
    if (len(node) is 0):
        return (string + "v")
    for param in node:
        string += get_type(param, False)
    return (string)

def get_specifier(node):
    if (hasattr(node._ctype, "_specifier")):
        if node._ctype._specifier <= 6 and \
           node._ctype._specifier >= 4:
            return node._ctype._specifier - 3
        elif node._ctype._specifier <= 3 and \
             node._ctype._specifier >= 1:
            return node._ctype._specifier - 1
    return 0

def get_sign(node):
    if (hasattr(node._ctype, "_sign")):
        if node._ctype._sign == 2:
            return 1
    return 0

def get_pointer(node, string, ctype_val):
    if (hasattr(node, "_decltype") and \
        node._decltype.__class__.__name__ == "QualType"):
        node = node._decltype._decltype
    else :
        node = node._decltype
    if ((hasattr(node, "_decltype") and \
         (node._decltype.__class__.__name__ == "PointerType") or \
             node._decltype.__class__.__name__ == "ArrayType") or \
        ((hasattr(node._decltype, "_decltype") and \
          node._decltype.__class__.__name__ == "QualType" and \
         (node._decltype._decltype.__class__.__name__ == "PointerType" or \
          node._decltype._decltype.__class__.__name__ == "ArrayType")))):
        if (ctype_val is '*'):
            return ctype_val
        string += get_pointer(node, ctype_val, ctype_val)
    return (string)

def marvin(node):
    rslt = "_" + get_type(node, False)
    rslt += get_name(node)
    rslt += get_params(node)
    return (rslt)

def mangleAttr(declaration, mod_name):
    mangled_name = "_" + str(len(mod_name)) + mod_name
    mangled_name += marvin(declaration)
    declaration._name = mangled_name
