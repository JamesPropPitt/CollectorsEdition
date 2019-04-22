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