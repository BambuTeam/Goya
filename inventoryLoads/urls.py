from django.urls import path
from inventoryLoads import views


urlpatterns = [
    path(
        route='provider/',
        view=views.provider_feed,
        name='inventory_provider'
    ),
    path(
        route='provider/new',
        view=views.provider_new,
        name='inventory_provider_new'
    ),
    # path(
    #   route='provider/newc',
    #   view=views.ProviderNew.as_view(),
    #   name='inventory_provider_newc'
    # ),
    path(
        route='provider/edit/<int:pk>',
        view=views.provider_edit,
        name='inventory_provider_edit'
    ),
    # path(
    #    route='provider/delete/<int:pk>',
    #    view=views.ProviderDelete.as_view(),
    #    name='inventory_provider_delete'
    # ),
    path(
        route='provider/delete/<int:pk>',
        view=views.provider_delete,
        name='inventory_provider_delete'
    ),
    path(
        route='',
        view=views.inventoryload_feed,
        name='inventory_load_feed'
    ),
    path(
        route='<int:pk>',
        view=views.inventoryLoad_detail,
        name='inventory_load_detail'
    ),
    path(
        route='new',
        view=views.InventoryCreateview.as_view(),
        name='inventory_new'
    )
]
