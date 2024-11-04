from datetime import timezone

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db import models
class Task(models.Model):
    title= models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class StudentList(models.Model):
    Register_Number= models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.Register_Number

    class User(models.Model) :
        username = models.CharField(max_length=150, unique=True)
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=128)

from django.db import models

class FeedbackForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    comments = models.CharField(max_length=150)

    def __str__(self):
        return f'Feedback from {self.name}'


class EmailInvitation(models.Model) :
    subject = models.CharField(max_length=255)
    body = models.TextField()

    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)

    def __str__(self) :
        return f'Invitation to {self.student.name} on {self.sent_at}'
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Adjust the max_length as needed
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
