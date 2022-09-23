from pickle import TRUE
from django.db import models


# Create your models here.

class School(models.Model):
    # xy=models.manager()

    sch_name=models.CharField(max_length=70)
    prcpl_name=models.CharField(max_length=70, default='xyz')

    def __str__(self):
        return self.sch_name

class Books(models.Model):
    b_name=models.CharField(max_length=70)

class Section(models.Model):
    class_tech_name=models.CharField(max_length=70,default='xyz')
    sec_name=models.CharField(max_length=70)
    b_name=models.ManyToManyField(Books)
    lecture_techer_name=models.CharField(max_length=70,default='xyz')
    
class Teacher(models.Model):
    t_name=models.CharField(max_length=70)
    join_date=models.DateField()
    sub_name=models.ManyToManyField(Books)  #, max_length=70, null=True,blank=True
    sch_name=models.ForeignKey(School,on_delete=models.CASCADE, null=True, blank=True)

class Student(models.Model):
    st_name=models.CharField(max_length=70)
    st_class=models.IntegerField()
    sch_name=models.ForeignKey(School,max_length=70,on_delete=models.CASCADE,null=True, blank=True)














