from django.db.models import Sum
from financial_control.main.models import Record, RecordEntry
from financial_control.main.forms import RecordForm, RecordEntryForm


def create_root_record(user, name) -> Record:
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


def get_dashboard_data_entries(user, entry_type):

    recordEntries = RecordEntry.objects.get_user_record_entries(user=user).filter(
        entry_type=entry_type
    )

    entriesSum = (
        recordEntries.aggregate(
            sum_january=Sum("january"),
            sum_february=Sum("february"),
            sum_march=Sum("march"),
            sum_april=Sum("april"),
            sum_may=Sum("may"),
            sum_june=Sum("june"),
            sum_july=Sum("july"),
            sum_august=Sum("august"),
            sum_september=Sum("september"),
            sum_octuber=Sum("octuber"),
            sum_november=Sum("november"),
            sum_december=Sum("december"),
        )
        if recordEntries.count() > 0
        else {
            "sum_january": 0,
            "sum_february": 0,
            "sum_march": 0,
            "sum_april": 0,
            "sum_may": 0,
            "sum_june": 0,
            "sum_july": 0,
            "sum_august": 0,
            "sum_september": 0,
            "sum_octuber": 0,
            "sum_november": 0,
            "sum_december": 0,
        }
    )

    entriesAnnualSum = sum([entriesSum[k] for k in entriesSum])
    entriesMean = round(entriesAnnualSum / 12, 2)

    return {
        "entries": recordEntries,
        "sum": {
            "month": entriesSum,
            "annual": entriesAnnualSum,
            "mean": entriesMean,
        },
    }


def get_dashboard_data(user):

    data = dict()
    data["expense"] = get_dashboard_data_entries(
        user=user, entry_type=RecordEntry.EntryType.EXPENSE
    )
    data["income"] = get_dashboard_data_entries(
        user=user, entry_type=RecordEntry.EntryType.INCOME
    )

    data["overview"] = {
        "assets": data["income"]["sum"]["annual"],
        "liabilities": data["expense"]["sum"]["annual"],
        "equity": data["income"]["sum"]["annual"] - data["expense"]["sum"]["annual"],
    }

    return data
