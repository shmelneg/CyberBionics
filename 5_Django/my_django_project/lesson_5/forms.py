from django import forms
from django.forms import ModelForm
from .models import Review



class InputForm(forms.Form):
    login = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['photo', 'email', 'description', 'score', 'feedback', 'phone']