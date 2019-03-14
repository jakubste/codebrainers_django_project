from django.contrib.auth.views import LogoutView
from django.urls import path

from wykop.accounts.views import RegisterView, UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('rejestracja', RegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
