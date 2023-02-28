from django.urls import path

from .views import show_tree_menu

urlpatterns = [
    path('', show_tree_menu, name='menu')
]
