from medicSearch.models import *

# Create your models here.


class State(models.Model):
    name = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
