from django.contrib.auth.forms import (
    AuthenticationForm as DjAuthenticationForm,
    UserCreationForm as DjUserCreationForm,
    UsernameField
)
from django.contrib.auth import get_user_model


class AuthenticationForm(DjAuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["class"] = "form-control"


class UserCreationForm(DjUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}
