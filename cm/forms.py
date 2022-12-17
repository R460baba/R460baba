from django import forms
from .models import student
class user(forms.ModelForm):
    username=forms.CharField()
    age=forms.IntegerField()
    gender=forms.CharField()
    phone=forms.IntegerField()
    email=forms.IntegerField()
    class Meta:
        model=student
        fields='__all__'
