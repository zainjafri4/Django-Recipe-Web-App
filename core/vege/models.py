from django.db import models
from django.contrib.auth.models import User

class rec(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rec_name = models.CharField(max_length=100)
    rec_dec = models.TextField()
    rec_image = models.ImageField(null=True, upload_to="rec_folder")

class Department(models.Model):
    department = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

class studentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class student(models.Model):
    department = models.ForeignKey(Department, related_name = "dept", on_delete=models.CASCADE)
    student_id = models.OneToOneField(studentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"


