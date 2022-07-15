from django import forms #importing django inbuilt form
from todo.models import Contact, Todo #attatching table where todo is app name and model is pyfilename
# and importing Todo class or table from pyfile

# a form structure for user entry

class TodoForm(forms.ModelForm): #Modelform user se entry leta h
    class Meta: # meta is for multiple inputs
        model=Todo #assigining the table
        fields={"title","description","name"} #attatching the fields from models.py with form

class TodoContact(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","email","mobile","query"}