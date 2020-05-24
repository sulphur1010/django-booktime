from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=25)
    written=models.DateField()
    created=models.DateTimeField(default=timezone.now)
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    thumnail=models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name} by {self.author}"


