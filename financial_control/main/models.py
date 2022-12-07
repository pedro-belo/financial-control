from financial_control.main.managers import RecordManager, RecordEntryManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Record(models.Model):

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="user_record"
    )

    name = models.CharField(max_length=50)

    parent = models.ForeignKey(
        "Record",
        on_delete=models.CASCADE,
        related_name="parent_record",
        null=True,
        blank=True,
    )

    @property
    def is_root(self):
        return self.parent is None

    def records_count(self):
        return self.parent_record.count() + self.record_entry.count()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RecordManager()

    def january_sum(self):
        return sum([entry.january for entry in self.record_entry.all()])

    def february_sum(self):
        return sum([entry.february for entry in self.record_entry.all()])

    def march_sum(self):
        return sum([entry.march for entry in self.record_entry.all()])

    def april_sum(self):
        return sum([entry.april for entry in self.record_entry.all()])

    def may_sum(self):
        return sum([entry.may for entry in self.record_entry.all()])

    def june_sum(self):
        return sum([entry.june for entry in self.record_entry.all()])

    def july_sum(self):
        return sum([entry.july for entry in self.record_entry.all()])

    def august_sum(self):
        return sum([entry.august for entry in self.record_entry.all()])

    def september_sum(self):
        return sum([entry.september for entry in self.record_entry.all()])

    def octuber_sum(self):
        return sum([entry.octuber for entry in self.record_entry.all()])

    def november_sum(self):
        return sum([entry.november for entry in self.record_entry.all()])

    def december_sum(self):
        return sum([entry.december for entry in self.record_entry.all()])

    def annual_mean(self):
        entries = self.record_entry.all()
        num_entries = entries.count()
        return (
            round(sum([entry.annual_sum for entry in entries]) / num_entries, 2)
            if num_entries > 0
            else 0
        )

    def annual_sum(self):
        return sum(
            [
                self.january_sum()
                + self.february_sum()
                + self.march_sum()
                + self.april_sum()
                + self.may_sum()
                + self.june_sum()
                + self.july_sum()
                + self.august_sum()
                + self.september_sum()
                + self.octuber_sum()
                + self.november_sum()
                + self.december_sum()
            ]
        )

    class Meta:
        verbose_name = _("Record")
        verbose_name_plural = _("Records")
        db_table = "main_record"

    def __str__(self) -> str:
        return self.name


class RecordEntry(models.Model):

    class EntryType(models.IntegerChoices):
        EXPENSE = 1, _("Despesa")
        INCOME = 2, _("Renda")

    entry_type = models.PositiveSmallIntegerField(choices=EntryType.choices)

    name = models.CharField(max_length=80)

    year = models.PositiveBigIntegerField()

    parent = models.ForeignKey(
        "Record", on_delete=models.CASCADE, related_name="record_entry"
    )

    january = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    february = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    march = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    april = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    may = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    june = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    july = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    august = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    september = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    octuber = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    november = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    december = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    @property
    def annual_sum(self):
        return sum(
            [
                self.january
                + self.february
                + self.march
                + self.april
                + self.may
                + self.june
                + self.july
                + self.august
                + self.september
                + self.octuber
                + self.november
                + self.december
            ]
        )

    @property
    def mean(self):
        amount = sum(
            [
                self.january
                + self.february
                + self.march
                + self.april
                + self.may
                + self.june
                + self.july
                + self.august
                + self.september
                + self.octuber
                + self.november
                + self.december
            ]
        )
        return round(amount / 12, 2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RecordEntryManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = (
            "parent",
            "name",
        )
        verbose_name = _("Record Entry")
        verbose_name_plural = _("Records Entries")
        db_table = "main_record_entry"


# RecordEntryDetail
