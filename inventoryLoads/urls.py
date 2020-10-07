from django.urls import path, include
from inventoryLoads import views


urlpatterns = [
    path(
        route = 'provider/',
        view = views.provider_feed,
        name = 'inventori_provider'
    ),
    path(
        route = 'provider/new',
        view = views.provider_new,
        name = 'inventori_provider_new'
    ),
]