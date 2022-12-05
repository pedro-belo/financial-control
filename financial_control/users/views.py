from django.db.transaction import atomic
from financial_control.main import facade

from django.contrib.auth.views import (
    LoginView as DjLoginView,
    LogoutView as DjLogoutView,
)
from django.views.generic import FormView
from financial_control.users.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse


class LoginView(DjLoginView):
    template_name = "login.html"
    form_class = AuthenticationForm


class LogoutView(DjLogoutView):
    pass


class UserCreationView(FormView):
    form_class = UserCreationForm
    template_name = "register.html"

    @atomic
    def form_valid(self, form):
        user = form.save()
        facade.create_root_record(user=user, name="Histórico Financeiro")
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("main:dashboard")
