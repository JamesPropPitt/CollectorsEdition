from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        # This gets the size of the image of the user's profile and scales it down to 300x300 pixels. This is because the size of the thumbnail is a circle of about 300x300 pixels
        # so any image bigger than that would take up unnecessary space on the website's storage and slow the website down.

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    studentnum = models.CharField(max_length=10)
    def __str__(self):
        return "{} {} ({})".format(self.firstname, self.lastname, self.studentnum)


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
