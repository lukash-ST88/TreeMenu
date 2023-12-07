from django import template
from ..functions.templatetag_functions import get_children_for_each_level_selected_submenu, get_selected_submenu_hierarchy
from ..models import SubMenu

register = template.Library()


@register.inclusion_tag('menu/tree_menu.html', takes_context=True)
def draw_menu(context, main_menu):
    try:
        submenus = SubMenu.objects.filter(main_menu__title=main_menu)
        high_level_submenus = [high_submenu for high_submenu in submenus.filter(parent=None).values()]
        selected_submenu_id = int(context['request'].GET.get(main_menu))
        print('selected_submenu_id', selected_submenu_id, sep=': ')
        selected_submenu = submenus.get(id=selected_submenu_id)
        selected_submenu_hierarchy = get_selected_submenu_hierarchy(selected_submenu,
                                                                    selected_submenu_id,
                                                                    high_level_submenus)
        print('selected_submenu_hierarchy', selected_submenu_hierarchy, sep=': ')
        for submenu in high_level_submenus:
            if submenu['id'] in selected_submenu_hierarchy:
                submenu['children'] = get_children_for_each_level_selected_submenu(submenu['id'],
                                                                                   selected_submenu_hierarchy,
                                                                                   submenus.values())
        print('high_level_submenus', high_level_submenus, sep=': ')
        context_menu_dict = {'submenus': high_level_submenus}

    except:
        context_menu_dict = {
            'submenus': [submenu for submenu in SubMenu.objects.filter(main_menu__title=main_menu, parent=None)]
        }
    context_menu_dict['main_menu'] = main_menu
    return context_menu_dict



