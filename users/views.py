""" users views"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
# Exeptions
from django.db.utils import IntegrityError
# models
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import SigupForm
""" users view for api """

from rest_framework import status, viewsets 
from rest_framework.decorators import action 
from rest_framework.response import Response 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt




from users.serializers import UserLoginSerializer, UserModelSerializer


class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @csrf_exempt
    @action(detail=False, methods=['post'])
    def loginapi(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)




""" clases for viewsets for api """








""" end for api code"""


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail  view"""
    template_name = 'users/detail.html'
    slug_filed = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        return context


class SignupView(FormView):
    template_name = 'users/signup.html'
    from_class = SigupForm
    succes_url = reverse_lazy('users:login')

    def form_falid(self, form):
        """ save from data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biograpy', 'phone_number', 'picture']

    def get_ogject(self):
        return self.request.user.prfile

    def get_success_url(self):
        """ return to users profile """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """ logiin view"""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LoginView):
    template_name = 'users/login.html'


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')




