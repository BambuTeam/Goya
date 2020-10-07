from django import forms
from inventoryLoads.models import *

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields='__all__'
