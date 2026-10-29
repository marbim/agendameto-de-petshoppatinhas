from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from base.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrar/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('base.urls')),
    path('', include('reserva.urls')),
]
