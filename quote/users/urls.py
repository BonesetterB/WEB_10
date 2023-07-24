from django.urls import path
from .views import RegistView
from .forms import LoginAuthenchens
from django.contrib.auth.views import LogoutView,LoginView

app_name='users'

urlpatterns = [
    path('Registration/', RegistView.as_view(), name='Log'),
    path('sign/', LoginView.as_view(template_name='users/sign.html', form_class=LoginAuthenchens, redirect_authenticated_user=True), name='Sign'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
