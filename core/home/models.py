from django.db import models

class student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True)

class cars(models.Model):
    car_name=models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return f"{self.car_name} - {self.speed}"

  
