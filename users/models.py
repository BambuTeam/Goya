# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Profile(models.Model):
    """profile model.
        proxi model tat etends the base model from user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biograpy = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """para retornar el string enves del user name """

    def __str__(self):
        return self.user.username


