from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Nombre', min_length=5, max_length=100,
                           widget=forms.TextInput(attrs={
                               'class':'form-control',
                               'placeholder':'Escribe tu nombre'
                           }))
    email = forms.EmailField(required=True, min_length=5, max_length=100,
                             widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':'Escribe tu email'
                             }))
    content = forms.CharField(required=True, min_length=5, max_length=1000,
                              widget=forms.Textarea(attrs={
                                'class':'form-control',
                                'placeholder':'Escribe tu mensaje',
                                'rows':'4'
                              }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if 'gmail.com' not in email:
            raise forms.ValidationError('Dominio inválido')
        return email

