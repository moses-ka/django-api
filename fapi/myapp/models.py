from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    discription = models.TextField()
    dateEnrolled = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name