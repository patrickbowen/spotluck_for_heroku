from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Orders(models.Model):
    o_id = models.IntegerField()
    #b_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    #s_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    #PURCHASED_CHOICES = [(YES, 'Yes'), (NO, 'No')]
    #purchased = models.CharField(choices=PURCHASED_CHOICES, default=NO) ########################################
    purchased = models.CharField(max_length=100)

    def __str__(self):
        return self.o_id
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
