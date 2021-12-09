from django.db import models
from django.contrib.auth.models import User

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=300, null=True)
    remote_address = models.CharField(max_length=20, null=True)
    method = models.CharField(max_length=10, null=True)
    request = models.TextField(null=True)
    response = models.TextField(null=True)
    response_code = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remote_address + self.url

