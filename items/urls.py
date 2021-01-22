from django.urls import path
from items import views

urlpatterns = [
    path(
        route='',
        view=views.ItemsListView.as_view(),
        name = 'items_feed'
    ),
    path(
        route = 'dashboard',
        view = views.items_dashboard,
        name = 'items_dashboard'
    ),
    path(
        route='new',
        view=views.item_new,
        name='item_new'
    ),
    path(
        route='item/<int:pk>',
        view=views.ItemEdit.as_view(),
        name='items_update'
    ),
    path(
        route = 'categories/',
        view = views.categories_feed,
        name = 'categories_feed'
    ),
    path(
        route = 'categories/<int:pk>',
        view = views.CategoryEdit.as_view(),
        name = 'categories_edit'
    ),
    path(
        route = 'categories/new',
        view = views.CategoryCreate.as_view(),
        name = 'categories_new'
    ),
]
