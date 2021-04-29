from django import forms
from piidb.models import (Addresses)


class addressSelectForm(forms.ModelForm):

    class Meta:
        model = Addresses
        fields = "__all__"
