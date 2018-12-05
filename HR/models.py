from django.db import models

# Basic models adding by admin
class State(models.Model):
    idno = models.CharField(primary_key=True,max_length=4)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class City(models.Model):
    idno = models.CharField(primary_key=True,max_length=4)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Add_Jobs(models.Model):
    idno = models.CharField(primary_key=True, max_length=4)
    city_name = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)

# Registration model by admin
class HR_Registration(models.Model):
    idno = models.CharField(primary_key=True,max_length=4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    experience = models.IntegerField(null=True)
    doj = models.DateField()
    phone = models.IntegerField(null=True)
    Address = models.CharField(max_length=300)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Manager_Registration(models.Model):
    idno = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    experience = models.IntegerField(null=True)
    doj = models.DateField()
    phone = models.IntegerField(null=True)
    Address = models.CharField(max_length=300)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Interviewer_Registration(models.Model):
    idno = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    experience = models.IntegerField(null=True)
    doj = models.DateField()
    phone = models.IntegerField(null=True)
    Address = models.CharField(max_length=300)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

# class Applicant_Registration(models.Model):
#     idno = models.CharField(primary_key=True, max_length=4)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=60)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=20)
#     designation = models.CharField(max_length=50)
#     experience = models.IntegerField(null=True)
#     phone = models.IntegerField(null=True)
#     Address = models.CharField(max_length=300)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)

class Applicant_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True,max_length=60)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)

