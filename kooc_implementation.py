import copy


def module_implementation(module, current_block):
    print (str(module))
    for var_generic_name in module['var']:
        for var_real_name, var_info in module['var'][var_generic_name].items():
            node = copy.copy(var_info[1])
        node._ctype._storage = 0
        current_block.ref.body.append(node)
    for var_generic_name in module['init var']:
        for var_real_name, var_info in module['init var'][var_generic_name].items():
            node = copy.copy(var_info[1])
            node._ctype._storage = 0
            current_block.ref.body.append(node)
