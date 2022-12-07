from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    View,
    TemplateView,
    RedirectView,
)
from financial_control.main import facade
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "main/dashboard/entry_point.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["data"] = facade.get_dashboard_data(user=self.request.user)
        return kwargs


class RecordView(LoginRequiredMixin, DetailView):

    template_name = "main/record/detail.html"

    def get_queryset(self):
        return facade.Record.objects.get_user_records(user=self.request.user)


class CreateRecordView(CreateView):

    form_class = facade.RecordForm
    model = facade.Record
    template_name = "main/record/create.html"

    def get_parent(self):
        try:
            records = facade.Record.objects.get_user_records(user=self.request.user)
            return records.get(pk=self.kwargs["parent_id"])
        except facade.Record.DoesNotExist:
            raise Http404

    def form_valid(self, form):
        record = facade.create_record(
            form=form, user=self.request.user, parent=self.get_parent()
        )
        return redirect("main:record-detail", pk=record.id)


class EditRecordView(UpdateView):

    form_class = facade.RecordForm
    template_name = "main/record/edit.html"

    def get_queryset(self):
        return facade.Record.objects.get_user_records(user=self.request.user)

    def get_success_url(self) -> str:
        record = self.get_object()
        return reverse("main:record-detail", kwargs={"pk": record.id})


class DeleteRecordView(RedirectView):
    def post(self, _, pk):
        try:
            records = facade.Record.objects.get_user_records(
                user=self.request.user, use_root_records=False
            )
            record = records.get(pk=pk)

            parent_id = record.parent_id
            record.delete()

            return redirect("main:record-detail", pk=parent_id)

        except facade.Record.DoesNotExist:
            raise Http404


class EditRecordEntryView(UpdateView):

    form_class = facade.RecordEntryForm
    template_name = "main/record_entry/edit.html"

    def get_queryset(self):
        return facade.RecordEntry.objects.get_user_record_entries(
            user=self.request.user
        )

    def get_success_url(self) -> str:
        record_entry = self.get_object()
        return reverse("main:record-detail", kwargs={"pk": record_entry.parent.id})


class CreateRecordEntryView(CreateView):

    form_class = facade.RecordEntryForm
    model = facade.RecordEntry
    template_name = "main/record_entry/create.html"

    def get_parent(self):
        records = facade.Record.objects.get_user_records(user=self.request.user)
        try:
            return records.get(pk=self.kwargs["parent_id"])
        except facade.Record.DoesNotExist:
            raise Http404

    def form_valid(self, form):
        parent = self.get_parent()
        _ = facade.create_record_entry(form=form, parent=parent)
        return redirect("main:record-detail", pk=parent.id)


class DeleteRecordEntryView(View):
    def post(self, _, pk):
        try:
            record_entries = facade.RecordEntry.objects.get_user_record_entries(
                user=self.request.user
            )
            record_entry = record_entries.get(pk=pk)

            parent_id = record_entry.parent_id
            record_entry.delete()

            return redirect("main:record-detail", pk=parent_id)

        except facade.Record.DoesNotExist:
            raise Http404
