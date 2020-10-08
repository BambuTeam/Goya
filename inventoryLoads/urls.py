from django.urls import path, include
from inventoryLoads import views


urlpatterns = [
    path(
        route = 'provider/',
        view = views.provider_feed,
        name = 'inventory_provider'
    ),
    path(
        route = 'provider/new',
        view = views.provider_new,
        name = 'inventory_provider_new'
    ),
    path(
        route = 'provider/edit/<int:pk>',
        view = views.provider_edit,
        name = 'inventory-provider_edit'
    ),
    path(
        route = '',
        view = views.inventoryload_feed,
        name = 'inventory_lodad_feed'
    ),
]