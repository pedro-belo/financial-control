from financial_control.users.models import User
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
    template_name = "users/login.html"
    form_class = AuthenticationForm

    @property
    def user_created(self):

        user_creation = self.request.session.get("user_creation", {})
        user = None

        if user_creation is not None:

            try:
                user = User.objects.get(pk=user_creation["user_id"])
                self.request.session["user_creation"] = {}

            except User.DoesNotExist:
                pass

            except KeyError:
                pass

        return user


class LogoutView(DjLogoutView):
    pass


class UserCreationView(FormView):
    form_class = UserCreationForm
    template_name = "users/register.html"

    @atomic
    def form_valid(self, form):

        user = form.save()
        facade.create_root_record(user=user, name="Histórico Financeiro")

        self.request.session["user_creation"] = {
            "confirm_account": False,
            "user_id": user.id,
        }

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("main:dashboard")
