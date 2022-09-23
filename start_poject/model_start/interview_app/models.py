from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Company(models.Model):
 
    #enum
    class Vacancy_In_Comp(models.TextChoices):  
        PYTHON='PY',_('Python')
        REACT='RE',_('React') 


    cmp_name=models.CharField(max_length=100,null=True,blank=True)  
    contact_no=models.CharField(max_length=10,null=True, blank=True) 
    vacancies=models.CharField(max_length=100,choices=Vacancy_In_Comp.choices,null=True,blank=True)
   
class Employee(models.Model):

    class Doc_In_Comp(models.TextChoices):  
        RESUME='RE',_('Resume')
        MARKSHEET='MR',_('Marksheet') 
      
    emp_name=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)
    document=models.CharField(max_length=100,choices=Doc_In_Comp.choices,null=True,blank=True)
    contact=models.CharField(max_length=10,null=True, blank=True) 
    cmp_name=models.ForeignKey(Company,max_length=100,on_delete=models.CASCADE,null=True, blank=True)
    #emp_name=models.ForeignKey(Employee,max_length=100,on_delete=models.CASCADE,null=True, blank=True)
    
    



    
    




                

