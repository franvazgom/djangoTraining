from django import forms


class ContactForm(forms.Form):
    # Valida que el nombre contenga al menos 5 caracteres
    name = forms.CharField(min_length=5)
    email = forms.EmailField()
    content = forms.CharField()
