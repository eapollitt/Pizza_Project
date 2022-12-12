from django import forms
from django.forms import ModelForm

class CommentForm(ModelForm):
    comment = forms.CharField(label='Comment', max_length=500)
