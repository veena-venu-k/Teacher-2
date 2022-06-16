from django import forms
from django.forms import ModelForm
from Teacher.models import Teacher

class TeacherAdd_Form(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"