from django.db import models
from django.conf import settings

class Prediction(models.Model):
    # optional link to user (null if guest)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    label = models.CharField(max_length=200)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label} ({self.confidence:.2f}) at {self.created_at}"
