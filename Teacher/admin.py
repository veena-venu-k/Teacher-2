from django.contrib import admin
from .models import Teacher

class TeaherAdmin(admin.ModelAdmin):
     list_display=('First_Name','Last_Name','Profile_Picture','Email_Address','Phone_Number','Room_Number','Subjects_taught')
     
# Register your models here.

admin.site.register(Teacher,TeaherAdmin)