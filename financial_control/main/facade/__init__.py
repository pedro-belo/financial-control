from financial_control.main.models import Record, RecordEntry
from financial_control.main.forms import RecordForm, RecordEntryForm

def create_root_record(user, name):
    return Record.objects.create(user=user, name=name)

def create_record(form, user, parent) -> Record:
    record = form.save(commit=False)
    record.user = user
    record.parent = parent
    record.save()
    return record

def create_record_entry(form, parent) -> RecordEntry:
    record_entry = form.save(commit=False)
    record_entry.parent = parent
    record_entry.save()
    return record_entry
