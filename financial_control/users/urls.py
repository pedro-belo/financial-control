from django.urls import path
from financial_control.users import views

app_name = 'users'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.UserCreationView.as_view(), name="register"),
    path("logout/", views.DjLogoutView.as_view(), name="logout")
]
