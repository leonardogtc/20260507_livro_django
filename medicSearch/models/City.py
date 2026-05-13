from medicSearch.models import *

# Create your models here.  


class City(models.Model):
    state = models.ForeignKey(State, null=True, blank=True,
                              related_name='State', on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)