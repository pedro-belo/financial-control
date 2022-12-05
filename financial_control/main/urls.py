from django.urls import path
from financial_control.main import views

app_name = "main"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("record/<int:pk>", views.RecordView.as_view(), name="record-detail"),
    path("record/<int:pk>/edit/", views.EditRecordView.as_view(), name="record-edit"),
    path(
        "record/<int:pk>/delete/",
        views.DeleteRecordView.as_view(),
        name="record-delete",
    ),
    path(
        "record/<int:parent_id>/create/",
        views.CreateRecordView.as_view(),
        name="record-create",
    ),
    path(
        "record-entry/<int:pk>/edit/",
        views.EditRecordEntryView.as_view(),
        name="record-entry-edit",
    ),
    path(
        "record-entry/<int:pk>/delete/",
        views.DeleteRecordEntryView.as_view(),
        name="record-entry-delete",
    ),
    path(
        "record-entry/<int:parent_id>/create/",
        views.CreateRecordEntryView.as_view(),
        name="record-entry-create",
    ),
]
