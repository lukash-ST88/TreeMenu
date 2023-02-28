def get_selected_submenu_hierarchy(selected_submenu, selected_submenu_id, high_level_submenus):
    selected_submenu_hierarchy = []
    while selected_submenu:
        selected_submenu_hierarchy.append(selected_submenu.id)
        selected_submenu = selected_submenu.parent
    if not selected_submenu_hierarchy:
        for menu in high_level_submenus:
            if menu['id'] == selected_submenu_id:
                selected_submenu_hierarchy.append(selected_submenu_id)
    return selected_submenu_hierarchy


def get_children_for_each_level_selected_submenu(selected_submenu_id, selected_submenu_hierarchy, all_submenus):
    single_level_submenus = [submenu for submenu in all_submenus.filter(parent_id=selected_submenu_id)]
    for submenu in single_level_submenus:
        if submenu['id'] in selected_submenu_hierarchy:
            submenu['children'] = get_children_for_each_level_selected_submenu(submenu['id'],
                                                                               selected_submenu_hierarchy, all_submenus)
    return single_level_submenus
