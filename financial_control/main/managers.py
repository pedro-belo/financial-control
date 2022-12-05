from django.db.models import QuerySet
from django.db.models import Manager

class RecordManager(Manager):

    def get_user_records(self, user, use_root_records=True) -> QuerySet:
        queryset = self.get_queryset().filter(user=user)
        return queryset if use_root_records else queryset.filter(parent=None)

    def get_user_root_records(self, user):
        return self.get_user_records(user).filter(parent=None)

class RecordEntryManager(Manager):

    def get_user_record_entries(self, user) -> QuerySet:
        return self.get_queryset().filter(parent__user=user)
