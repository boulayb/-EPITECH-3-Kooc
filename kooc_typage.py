from cnorm import nodes
from collections import ChainMap

def findType(val):

    if "\"" in val:
        return ["C", {"char *": ["char *"]}]
    elif "." in val:
        return ["C", {"float": ["float"]}]
    else:
        return ["C", {"int": ["int"]}]

def countPointer(ast, typedict, name):

    if type(ast._decltype) == nodes.PointerType:
        typedict["_"][name][name][0] += "*"
        countPointer(ast._decltype, typedict, name)

def getSignature(expr, typedict):

    signdict = list()

    if expr.value.find(".") > -1:
        split = expr.value.split(".")
        signdict.append("KC")
        signdict.append(typedict[split[0]][split[1]])
    elif expr.value.find(" ") > -1:
        split = expr.value.split(" ")
        signdict.append("KC")
        signdict.append(typedict[split[0]][split[1]])
    else:
        signdict.append("C")
        signdict.append(typedict["_"][expr.value])

    return signdict

def typeId(ast, signdict):

    if signdict[0] == "KC":
        if len(signdict[1]) == 1:
            ast.value = next(iter(signdict[1].keys()))
        else:
            raise ValueError("Type checking failed.\n")

def getRetType(signdict):

    for key, val in signdict:
        signdict[key] = list(val[-1])

    return signdict

def typeFunc(ast, typedict, signdict):

    paramTab = list()

    for idx, param in enumerate(ast.params):
        if type(ast) == nodes.Binary and idx == 0:
            continue
        # elif type(param) == nodes.Binary:
        #     typeFunc(param, typedict, getSignature(param.params[0], typedict))
        #     if param.params[0].hasattr("KoocIDs"):
        #         KoocIDs = getattr(param.params[0], "KoocIDs")
        #         if len(KoocIDs) == 1:
        #             paramTab.append(KoocIDs.iterkeys().next())
        #         else:
        #             paramTab.append(KoocIDs)
        elif type(param) == nodes.Func:
            paramTab.append(getRetType(getSignature(param.call_expr, typedict)[1]))
            # typeFunc(param, typedict, getSignature(param.call_expr, typedict))
        elif type(param) == nodes.Literal:
            paramTab.append(findType(param.value))
        elif type(param) == nodes.Id:
            paramTab.append(getSignature(param, typedict))

    rslt = list()

    for key, val in signdict[1].items():
        save = paramTab
        if type(ast) == nodes.Func:
            val.pop()
        for idx, sign in enumerate(val):
            foundFlag = 0
            for key2, val2 in paramTab[idx][1].items():
                if sign == val2[0]:
                    paramTab[idx][1] = {key2: val2}
                    foundFlag = 1
                    break
            if foundFlag == 0:
                paramTab = save
                break
        if foundFlag == 1:
            rslt.append({key: paramTab})
            paramTab = save

    if len(rslt) == 1:
        for idx, param in enumerate(ast.params):
            if param == ast.params[0]:
                if type(ast) == nodes.Binary:
                    ast.params[0].value = next(iter(rslt[0].keys()))
                    continue
                elif type(ast) == nodes.Func:
                    ast.call_expr.value = next(iter(rslt[0].keys()))
            if next(iter(rslt[0].items()))[idx][0] == "KC":
                param.value = next(iter(next(iter(rslt[0].items()))[idx][1].keys()))
    else:
        raise ValueError("Type checking failed.\n")

    # if type(rslt) == str:
    #     expr.params[idx].value = rslt
    # elif type(rslt) == dict and len(rslt) > 0:
    #     if len(rslt) == 1 and KoocIDs in locals():
    #         binaryExpr(param, typedict)
    #         setattr(expr.params[idx], "KoocIDs", rslt)
    #     else:
    #         raise ValueError("Type checking failed.\n")

def parseBlockStmt(ast, typedict):

    for line in ast:

        if type(line) == nodes.Decl:
            typedict["_"][line._name] = {}
            typedict["_"][line._name][line._name] = list()
            typedict["_"][line._name][line._name].append(line._ctype._identifier)
            if type(line._ctype._decltype) == nodes.PointerType:
                typedict["_"][line._name][line._name][0] += " *"
                countPointer(line._ctype._decltype, typedict, line._name)
            if hasattr(line._ctype, "_params"):
                for param in reversed(line._ctype._params):
                    typedict["_"][line._name][line._name].insert(0, param._ctype._identifier)
                    if type(param._ctype._decltype) == nodes.PointerType:
                        typedict["_"][line._name][line._name][0] += " *"
                        countPointer(param._ctype._decltype, typedict, line._name)
            if hasattr(line, "body"):
                typedict["_"] = typedict["_"].new_child()
                parseBlockStmt(line.body.body, typedict)

        elif type(line) == nodes.ExprStmt:
            if type(line.expr) == nodes.Id:
                typeId(line.expr, getSignature(line.expr, typedict))
            elif type(line.expr) == nodes.Func:
                typeFunc(line.expr, typedict, getSignature(line.expr.call_expr, typedict))
            elif type(line.expr) == nodes.Binary:
                typeFunc(line.expr, typedict, getSignature(line.expr.params[0], typedict))

        elif type(line) == nodes.BlockStmt:
            typedict["_"] = typedict["_"].new_child()
            parseBlockStmt(line.body, typedict)

    typedict["_"] = typedict["_"].parents

def typage(ast, typedict):

    typedict["_"] = ChainMap({})

    parseBlockStmt(ast.body, typedict)

    return ast
