from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True);
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50);
    last_name = models.CharField(max_length=50);
    email = models.EmailField(max_length=100);
    phone_number = models.CharField(max_length=50);
    address = models.TextField(max_length=50);
    city = models.CharField(max_length=50);
    state = models.CharField(max_length=50);
    zip_code = models.CharField(max_length=50);

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}");