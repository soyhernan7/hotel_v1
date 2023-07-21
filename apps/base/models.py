from django.db import models

from simple_history.models import HistoricalRecords


# Create your models here.
class BaseModel(models.Model):
    """Model definition for BaseModel."""

    id = models.AutoField(primary_key=True)
    active = models.BooleanField('Active', default=True)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)
    modified_date = models.DateTimeField('Updated Date', auto_now=True)
    deleted_date = models.DateTimeField('Deleted Date', null=True, blank=True)
    history = HistoricalRecords(user_model="user.User", inherit=True)

    class Meta:
        abstract = True
        ordering = ['-created_date']
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

