from django.urls import path
from .views import RegistView
from .forms import LoginAuthenchens
from django.contrib.auth.views import LogoutView,LoginView

app_name='users'

urlpatterns = [
    path('Registration/', RegistView.as_view(), name='Log'),
    path('sign/', LoginView.as_view(template_name='users/sign.html', form_class=LoginAuthenchens, redirect_authenticated_user=True), name='Sign'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url='/users/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
