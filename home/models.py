from django.contrib.auth import get_user_model
from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db import models
from django.urls import reverse
from django.conf import settings


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class IndexModel(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), blank=True,
                                 null=True, )

    def get_absolute_url(self):
        return reverse(
            "new-order", args=[self.username_id]
        )


class Order(models.Model):
    COLORS = (
        ("yellow", "yellow"),
        ("BABYBLUE", "BABYBLUE"),
        ("GREEN", "GREEN"),
    )
    STATE = (
        ("Giza", "Giza"),
        ("Cairo", "Cairo"),
    )

    colors = models.CharField(max_length=10, choices=COLORS, null=True, blank=True, default='GREEN')
    first_name = models.CharField(max_length=120, default='')
    last_name = models.CharField(max_length=120, default='')
    email = models.EmailField(validators=[validate_email], default='')
    address = models.CharField(max_length=300, null=True, blank=True)
    address2 = models.CharField(max_length=300, blank=True, default='')
    state = models.CharField(max_length=10, choices=STATE, null=True, blank=True, default='Giza')
    user = models.ForeignKey(UserModel, on_delete=models.SET(get_sentinel_user), blank=True, null=True, )

    def get_absolute_url(self):
        return reverse("store:orders")


class SingleOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("store:item", args=[str(self.order.id)])



class Support(models.Model):
    title = models.CharField(max_length=120, )
    email = models.EmailField(validators=[validate_email])
    body = models.TextField()

    @staticmethod
    def get_absolute_url():
        return reverse("store:home")

    def __str__(self):
        return self.title + ' | ' + str(self.email)
