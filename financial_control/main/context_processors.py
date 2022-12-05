from financial_control.main import facade
from django.template import RequestContext


def main_ctx(request):

    user = request.user
    root_records = (
        facade.Record.objects.get_user_root_records(user=user)
        if user.is_authenticated
        else facade.Record.objects.none()
    )

    return {"root_records": root_records}
