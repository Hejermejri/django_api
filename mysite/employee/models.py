from django.db import models

# Create your models here.
class Employee(models.Model):
    emplyee_regNo = models.TextField(unique=True)
    emplyee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)


    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)
def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"