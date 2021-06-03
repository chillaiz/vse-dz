from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from home_work.models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=15,
                           required=True, label='Категория',
                           widget=TextInput(
                               attrs={
                                   'placeholder': 'Название категории'
                               }
                           ))

    def clean_name(self):
        name = self.cleaned_data['name']
        print(name)
        category = Category.objects.filter(name=name)
        if category.count()>0:
            raise ValidationError('уже есть!')
        return name
