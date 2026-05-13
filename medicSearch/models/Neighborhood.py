from medicSearch.models import *
from medicSearch.models.City import City

# Create your models here.


class Neighborhood(models.Model):
    city = models.ForeignKey(City, null=True, blank=True,
                             related_name='City', on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.city.name)
