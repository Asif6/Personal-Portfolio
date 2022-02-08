from audioop import maxpp
from operator import mod
from pydoc import describe
from pyexpat import model
from turtle import color
from django.db import models
from django.shortcuts import render

# Create your models here.

class username(models.Model):
    user_full_name=models.CharField(max_length=200)

    user_img=models.FileField(upload_to='media/user/user_img',default="NONE")

    def __str__(self):
        return self.user_full_name

class profession(models.Model):
    user_profession=models.CharField(max_length=200)
    def __str__(self):
        return self.user_profession

class SocialLinks(models.Model):
    fontawesomeIcone=models.CharField(max_length=500)
    links=models.CharField(max_length=90000000)

class AboutMe(models.Model):
    img=models.ImageField(upload_to='media/user')
    cv=models.FileField(upload_to='media/user/Files')
    description=models.TextField(max_length=400)


class Skills(models.Model):
    title=models.CharField(max_length=100)
    percentage =models.IntegerField()
    data_color=models.CharField(max_length=50,default="FFD15C")
    def __str__(self):
        return self.title


class Workingjourney(models.Model):
    Projects_completed=models.IntegerField()
    Cup_of_coffee=models.IntegerField()
    Satisfied_clients=models.IntegerField()
    

class ServicesColor(models.Model):
    color=models.CharField(max_length=50)
    shadow= models.CharField(max_length=50)

    def __str__(self) :
        return f"Color= {str(self.color)} | Shadow= {str(self.shadow)}"

class Services(models.Model):

    img=models.FileField(upload_to='media/user/Services')
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=3000)
    color=models.ForeignKey(ServicesColor,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
        
class Educations(models.Model):
    time=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self) -> str:
        return f'{str(self.time)} | {str(self.degree)}'


class JobExperience (models.Model):
    time=models.CharField(max_length=100)
    jobTitle=models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self) -> str:
        return f'{str(self.time)} | {str(self.jobTitle)}'
