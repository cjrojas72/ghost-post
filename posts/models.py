from django.db import models
from django.utils import timezone


CHOICE = (
    (True, 'boasts'),
    (False, 'roasts')
)


class Post(models.Model):
    name = models.CharField(max_length=50)
    choice = models.BooleanField(choices=CHOICE, default=True, blank=False)
    user_input = models.TextField()
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
