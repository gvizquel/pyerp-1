# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# Librerias en carpetas locales
from ..views import (
    ActivateView, AvatarUpdateView, ChangePasswordView, LogOutModalView,
    PasswordRecoveryView, ProfileView, SignUpView)

urlpatterns = [
    # ================= Rutas de Auto Gestion de Usuarios ================== #
    path('signup', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activar'),
    path(
        'login/',
        LoginView.as_view(
            template_name='usercustom/login.html',
            # redirect_field_name='next',
            success_url='home'
        ),
        name='login'
    ),
    path(
        'logout',
        LogoutView.as_view(next_page='base:login'),
        name='logout'
    ),
    path('logoutmodal/', LogOutModalView.as_view(), name='logout-modal'),
    path('profile', login_required(ProfileView.as_view()), name='profile'),
    path(
        'changepasword',
        login_required(ChangePasswordView),
        name='change-password'
        ),
    path(
        'password-recovery',
        PasswordRecoveryView.as_view(),
        name='password-recovery'
    ),
    path(
        'password-recovery/<uidb64>/<token>',
        PasswordRecoveryView.as_view(),
        name='password-set'
    ),
    path('avatar', login_required(AvatarUpdateView.as_view()), name='avatar'),
]