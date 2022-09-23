from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display=['sch_name','prcpl_name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['t_name','join_date','sch_name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['st_name','sch_name','st_name']

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display=['b_name']


@admin.register(Section)
class sectionAdmin(admin.ModelAdmin):
    list_display=['sec_name','lecture_techer_name','class_tech_name']

# @admin.register(Dog)
# class sectionAdmin(admin.ModelAdmin):
#     list_display=['name','data']


