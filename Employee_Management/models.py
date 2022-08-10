from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    Fname = models.CharField(max_length=100, null=False)
    Lname = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=False)
    salary = models.IntegerField(default = 0)
    bonus = models.IntegerField(default = 0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=False)
    phone = models.IntegerField(default=0,null=False)
    hire_date = models.DateField()
     

    def __str__(self):
        return f'{self.Fname} {self.Lname} {self.phone}'







