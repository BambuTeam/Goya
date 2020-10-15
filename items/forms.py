from django import forms
from items.models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class CategoryForm(forms.Form):
    model = Category
    fields = ('name', 'description')