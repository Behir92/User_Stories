from django.db import models

# Create your models here.
TYPE= (
    (1,"domowy"),
    (2,"służbowy"),
    (3,"komórkowy"),
    )




class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.TextField()
    
    
class Adress(models.Model):
    person = models.ForeignKey(Person)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    house_number = models.IntegerField()
    apt_number = models.IntegerField()    

class Telephone(models.Model):
    person = models.ForeignKey(Person)
    number = models.CharField(max_length=128)
    type = models.IntegerField(choices=TYPE)
    
    
class Email(models.Model):
    person = models.ForeignKey(Person)
    adr_email = models.EmailField(max_length=128)
    type = models.IntegerField(choices=TYPE)
    