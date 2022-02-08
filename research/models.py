import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Conversion(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    input = models.TextField()
    output = models.TextField(
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    converted_at = models.DateTimeField(
        null=True,
    )
    if_finished = models.BooleanField(default=False)
    progress = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
