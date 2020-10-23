from django.urls import path
from dashboard import views

urlpatterns = [
    path(
        route='',
        view=views.welcome,
        name = 'welcome'
    ),
]