def create_diff(tree1, tree2):
    result = []
    tree1_keys, tree2_keys = tree1.keys(), tree2.keys()
    all_keys = sorted(list(set(tree1_keys) | set(tree2_keys)))
    added_keys = tree2_keys - tree1_keys
    deleted_keys = tree1_keys - tree2_keys
    for key in all_keys:
        item = {'key': key}
        value1 = tree1.get(key)
        value2 = tree2.get(key)
        if key in added_keys:
            item['status'] = 'added'
            item['new_value'] = value2
        elif key in deleted_keys:
            item['status'] = 'deleted'
            item['old_value'] = value1
        elif isinstance(value1, dict) and isinstance(value2, dict):
            item['status'] = 'nested'
            item['nested'] = create_diff(value1, value2)
        elif value1 == value2:
            item['status'] = 'equal'
            item['old_value'] = value1
        else:
            item['status'] = 'changed'
            item['old_value'] = value1
            item['new_value'] = value2
        result.append(item)
    return result
