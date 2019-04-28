from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
# This creates the class and the rules on what a 'post' is... Hopefully it's self explanatory.
# This _get_absolute_url definition is something semi-built into django which allows the user to be redirected after creating a post without having to handle post requests and save information.

class Sprint(models.Model):
    NoSprint = 'SprintNo0'
    Sprint1 = 'SprintNo1'
    Sprint2 = 'SprintNo2'
    Sprint3 = 'SprintNo3'
    Sprint4 = 'SprintNo4'
    Sprint5 = 'SprintNo5'
    Sprint_Number_Choices=(
        (NoSprint, 'No Sprint Selected'),
        (Sprint1, 'Sprint 1'),
        (Sprint2, 'Sprint 2'),
        (Sprint3, 'Sprint 3'),
        (Sprint4, 'Sprint 4'),
        (Sprint5, 'Sprint 5'),
    )
    Sprint_Number = models.CharField(
        max_length=9,
        choices=Sprint_Number_Choices,
        default= NoSprint,
    )
    # I'm not sure how many sprints there are or will be in a term, but you can easily change how many there are by adding more sprints to this list or removing them.

