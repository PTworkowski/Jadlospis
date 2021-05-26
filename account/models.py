from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image
import uuid

class MyUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(default='defalult.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=120, default="", null=True, blank=True)
    building = models.CharField(max_length=20, default="", null=True, blank=True)
    apartment = models.CharField(max_length=20, default="", null=True, blank=True)
    city = models.CharField(max_length=20, default="", null=True, blank=True)
    zip_code = models.CharField(max_length=6, default="", null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)