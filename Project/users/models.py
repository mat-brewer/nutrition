from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    current_weight_lbs = models.DecimalField(default=0, max_digits=4, decimal_places=1)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, **kwargs):
        super().save()

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.profile_picture.path)