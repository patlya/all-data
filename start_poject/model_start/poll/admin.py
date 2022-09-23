from django.contrib import admin

from .models import *

admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Student)
admin.site.register(Vehicle)

admin.site.register(hello)
admin.site.register(Animal)
admin.site.register(Validation_error)
admin.site.register(Apply_field)
admin.site.register(Intrest)
admin.site.register(Person_detail)
admin.site.register(City)
admin.site.register(PersonAddress)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Person_through)
admin.site.register(Group_through)
admin.site.register(Membership)
admin.site.register(Person_DoB)
admin.site.register(method_over)
admin.site.register(Student1)
#admin.site.register(School)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['s_name','join_date','t_name','salary']

@admin.register(Student_abs)
class Student_absAdmin(admin.ModelAdmin):
    list_display=['s_name','join_date','st_name','fees']


#admin_name=admin
#pswd=admin 
# Register your models here.
