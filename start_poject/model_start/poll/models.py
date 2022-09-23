from multiprocessing.sharedctypes import Value
from random import choices
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Musician(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    instrument=models.CharField(max_length=100)


class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    release_date=models.DateField(default=datetime.now)
    num_stars=models.IntegerField()  

class Vehicle(models.Model):
   geeks_field = models.CharField(max_length = 200, null = True, blank=True,db_column="col_1",default="GfG is bets",help_text="Please use the following format: <em>YYYY-MM-DD</em>.")       
   #geeks_field = models.CharField(max_length = 200, )

class hello(models.Model):   
   x_field=models.IntegerField(primary_key=True,editable=False)

class Student(models.Model):
     

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    LIST_CHOICE=[
        ('School_student',
            (

                ('FR' ,'Fresher'),
                ('JR' ,'Junior'),
                ('SR' ,'Senior'),
                ('GR' ,'Graduate'),
            )
        ),
         ('clg_student',
            (

                ('FR' ,'Fresher'),
                ('JR' ,'Junior'),
                ('SR' ,'Senior'),
                ('GR' ,'Graduate'),
            )
        ),
        
    ]
    year_in_school=models.CharField(max_length=2,choices=LIST_CHOICE,default='FR') 


class Animal(models.Model):
    z_field=models.CharField(max_length=200,unique=True,error_messages={'unique':'please enter correct data'},verbose_name="geeks_new_name")


from django.core.exceptions import ValidationError

def Validation_define(value):
    if "@gmail.com" in value:
        return Value

    else:
        raise ValidationError("This field accepts mail id of google only") 

class Validation_error(models.Model):
    geeks_mail = models.CharField(
                         max_length = 200,
                         validators =[Validation_define]
                         )  
                        

class Apply_field(models.Model):
    type_field=models.AutoField(primary_key=True,verbose_name="new_name_field") 
   

# Relationfields start now-------------------------

class Intrest(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Person_detail(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    intrests=models.ManyToManyField(Intrest,max_length=200)


    def __str__(self):
        return self.name

class City(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class PersonAddress(models.Model):
    person=models.OneToOneField(Person_detail,max_length=200,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    street_address=models.CharField(max_length=200)


    def __str__(self):
        return self.person.name+"(" + self.street_address +")"



#Additional ForeignKey Parameters
# 1.related_name="books"
# 2.related_query_name="book"
# 3.to_field='name'
class Author(models.Model):
    name=models.CharField(max_length=200) 


# Author.objects.get(id=2).books.all() we can  get author how many books right use related _name parameter 
#related_name='xyz'  , we get all values of author:-without related name=Author.book_set.all(), related name=author.xyz
class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,related_query_name="book")           
  

  # slugfield :-ex.ranupatlya=ranu-patlya in url 
  #pip install django autoslug
  #autoslugfield(populate_from="kisko slug krna he field dena he " unique ,null ,default)

class Person_through(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group_through(models.Model):
    name=models.CharField(max_length=50)
    members=models.ManyToManyField(Person_through,through='Membership')


    def __str__(self):
        return self.name

class Membership(models.Model): 
    person=models.ForeignKey(Person_through,max_length=200,on_delete=models.CASCADE)
    group=models.ForeignKey(Group_through,on_delete=models.CASCADE,max_length=200)   
    date_joined=models.DateField()
    invite_reason=models.CharField(max_length=200)  


#model methods :-

from datetime import datetime
class Person_DoB(models.Model):
    f_name=models.CharField(max_length=50)
    L_name=models.CharField(max_length=50)
    dob=models.DateField()


 
    #this method call instance of class Person_DoB 
    def ststus(self):
        if self.dob < datetime.date(1945, 8, 1):
            return "pre boomer"
        elif self.dob < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post_boomer"

     #Overriding predefined model methods

class method_over(models.Model):
    name=models.CharField(max_length=20)
    dt=models.DateTimeField()
    
    def save(self):
        self.dt = datetime.now()
        return super().save() 


#inheritance start now..............
#abstract class inheritance..............
class School(models.Model):
    s_name=models.CharField(max_length=200)
    join_date=models.DateField()
    
    #if you want to create abs class so compulsary to create meta class
    class Meta:
        abstract=True

class Teacher(School):
    t_name=models.CharField(max_length=20)
    salary=models.IntegerField()

    class Meta:
        ordering=['t_name']

class Student_abs(School):
    st_name=models.CharField(max_length=200)
    fees=models.IntegerField()
    #we can create custome manager
    new_manager=models.Manager()

    
    class Meta:
        ordering=['st_name']


class Student1(models.Model):
    sub_name=models.CharField(max_length=200,null=True,blank=True)
    total_marks=models.IntegerField()
    obtain_mark=models.IntegerField()


#a=Student1.objects.filter(total_marks__gt=F('obtain_mark')).annotate(diffr_mark=F('total_marks')-F('obtain_mark'))
# a[0].diffr_mark  (we got difrence between total_marks-obtain_marks)


















    
 