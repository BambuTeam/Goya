from django import forms
from items.models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class CategoryForm(forms.Form):
    model = Category
    fields = ('name', 'description')