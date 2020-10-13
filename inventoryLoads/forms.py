from django import forms
from inventoryLoads.models import *
from django.forms.models import inlineformset_factory


ChildFormset = inlineformset_factory(
    InventoryLoad, InventoryLoadDetail, fields=('item', 'quantity', 'price')
)


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields='__all__'


class InventoriLoadForm(forms.ModelForm):
    class Meta: 
        model = InventoryLoad
        fields = '__all__'


class InventoryLoadDetailForm(forms.ModelForm):
    class Meta:
        model = InventoryLoadDetail
        fields = '__all__'