from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your models here.
class Doc(models.Model):
    upload = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("disp", kwargs={"image_id": self.pk})
    