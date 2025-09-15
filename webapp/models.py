from django.db import models

# Create your models here.

class students(models.Model):
    fname=models.CharField(max_length=159);
    lname=models.CharField(max_length=159);
    email=models.CharField(max_length=159);
    phone=models.CharField(max_length=159);
    address=models.CharField(max_length=159);
    city=models.CharField(max_length=159);
    state=models.CharField(max_length=159);
    zip=models.CharField(max_length=159);
    gender=models.CharField(max_length=159);
    loginid=models.CharField(max_length=159);
    pass_word=models.CharField(max_length=159);
    department=models.CharField(max_length=159);


class faculty(models.Model):
    fname=models.CharField(max_length=159);
    lname=models.CharField(max_length=159);
    email=models.CharField(max_length=159);
    phone=models.CharField(max_length=159);
    address=models.CharField(max_length=159);
    department=models.CharField(max_length=159);

class library(models.Model):
    title=models.CharField(max_length=159);
    author=models.CharField(max_length=159);
    ISBN=models.CharField(max_length=159);
    location=models.CharField(max_length=159);

class books(models.Model):
    title=models.CharField(max_length=159);
    author=models.CharField(max_length=159);
    ISBN=models.CharField(max_length=159);
    bookstore=models.CharField(max_length=159);
    cost=models.IntegerField();


class room_request(models.Model):
    fname=models.CharField(max_length=159);
    lname=models.CharField(max_length=159);
    email=models.CharField(max_length=159);
    phone=models.CharField(max_length=159);
    loginid=models.CharField(max_length=159);
    gender=models.CharField(max_length=159);
    cost=models.IntegerField();
    dat_e=models.DateField();

class election(models.Model):
    name=models.CharField(max_length=159);
    image=models.CharField(max_length=159);
    votes=models.IntegerField();
    votesp=models.FloatField();

class mealplan(models.Model):
    fname=models.CharField(max_length=159);
    loginid=models.CharField(max_length=159);
    plan=models.CharField(max_length=159);
    fro_m=models.CharField(max_length=159);
    t_o=models.CharField(max_length=159);


class events(models.Model):
    name=models.CharField(max_length=159);
    description=models.CharField(max_length=159);
    dat_e=models.DateField();
 

class bookevents(models.Model):
    loginid=models.CharField(max_length=159);
    name=models.CharField(max_length=159);
    description=models.CharField(max_length=159);
    dat_e=models.DateField();
    eid=models.CharField(max_length=159);
 

class busticket(models.Model):
    typ_e=models.CharField(max_length=159);
    cost=models.CharField(max_length=159);
    dat_e=models.DateField();
    loginid=models.CharField(max_length=159);

