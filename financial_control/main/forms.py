from financial_control.main.models import Record, RecordEntry
from django.forms import ModelForm


class RecordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"

    class Meta:
        fields = ("name",)
        model = Record


class RecordEntryForm(ModelForm):
    class Meta:
        fields = (
            "name",
            "year",
            "entry_type",
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "octuber",
            "november",
            "december",
        )
        model = RecordEntry

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["entry_type"] = "form-select"
