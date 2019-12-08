from django import forms
from django.db import models
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "price", "quantity", "completed"]