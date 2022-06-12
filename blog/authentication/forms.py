from django.db import models  
from django.forms import fields  
from .models import blog  
from django import forms  
  
  
class newform(forms.ModelForm):  
    class meta:  
        models = blog
        # It includes all the fields of model  
        fields = '__all__'  