from django import forms

from kitchen.models import Cook


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["username", "password"]
