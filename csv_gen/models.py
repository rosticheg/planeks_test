from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):
    """User Schema"""
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=200)
    created = models.DateTimeField("Creation date", auto_now_add=True)
    modified = models.DateTimeField("Modification date", auto_now_add=True)
    file_name = models.FileField("Schema file", upload_to="media/", blank=True, null=True)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



