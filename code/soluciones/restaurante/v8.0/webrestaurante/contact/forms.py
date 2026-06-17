from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Nombre', min_length=5, max_length=100,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Escribe tu nombre'
                           }))
    email = forms.EmailField(required=True, min_length=5, max_length=100,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Escribe tu email'
                             }))
    content = forms.CharField(required=True, min_length=5, max_length=1000,
                              widget=forms.Textarea(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Escribe tu mensaje',
                                  'rows': '4'
                              }))

    # clean_nombre_del_campo
    def clean_email(self):
        email = self.cleaned_data['email']
        name = self.cleaned_data['name']
        if 'gmail.com' not in email:
            raise forms.ValidationError('dominio inválido')
        if name in email:
            raise forms.ValidationError(
                'El usuario no puede ser parte del email')
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        if name in email:
            raise forms.ValidationError(
                'El usuario no puede ser parte del email')
        return cleaned_data
