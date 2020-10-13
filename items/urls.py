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
        route='<int:pk>',
        view=views.item_update,
        name='items_update'
    ),
    path(
        route = 'categories/',
        view = views.categories_feed,
        name = 'categories_feed'
    ),
    path(
        route = 'categories/<int:pk>',
        view = views.categories_edit,
        name = 'categories_edit'
    )

]