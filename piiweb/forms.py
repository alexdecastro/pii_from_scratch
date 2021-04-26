from django import forms
from piidb.models import (Addresses)


class AddressesModelForm(forms.ModelForm):

    class Meta:
        model = Addresses
        fields = "__all__"
