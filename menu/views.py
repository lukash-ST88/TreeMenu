from django.shortcuts import render


def show_tree_menu(request):
    return render(request, 'menu/base.html')
