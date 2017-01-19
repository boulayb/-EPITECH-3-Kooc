import kooc_mangling

def is_composed(node):
    if node._ctype.__class__.__name__ is "ComposedType":
        return True
    return False

def is_func(node):
    if (node._ctype.__class__.__name__ == "FuncType"):
        return (True)
    return False

def is_var(node):
    if (node._ctype.__class__.__name__ == "PrimaryType"):
        return (True)
    return False

def is_typedef(node):
    if (hasattr(node._ctype, "_storage") and \
        node._ctype._storage == 2):
        return True
    return False

def is_init(node):
    if hasattr(node, "_assign_expr") :
        return True
    return False

def get_value(node):
    if hasattr(node, "_assign_expr"):
        if hasattr(node._assign_expr, "value") :
            return (node._assign_expr.value)
    return ""

def get_ctype(node):
    string = kooc_mangling.get_type(node, True)
    return string
