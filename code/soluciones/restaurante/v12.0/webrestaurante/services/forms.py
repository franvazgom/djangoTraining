from django.forms import ModelForm, TextInput, Textarea, NumberInput, EmailInput
from services.models import Service, Order
from django_ckeditor_5.widgets import CKEditor5Widget

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'sub_title', 'content', 'image','cost',]
        widgets = {
            'title':TextInput(attrs={'class':'form-control','placeholder':'Título'}),
            'sub_title':TextInput(attrs={'class':'form-control','placeholder':'Sub título'}),
            'content':CKEditor5Widget(config_name='extends'),
            'cost':NumberInput(attrs={'step': '0.01', 'placeholder': '0.00', 'class': 'form-control'}), 
        }
    
    def clean(self):
        super(ServiceForm, self).clean()
        title = self.cleaned_data['title']
        if len(title) < 5:
            self._errors['title'] = self.error_class(['Mínimo 5 caracteres'])
        return self.cleaned_data

class OrderForm(ModelForm): 
    class Meta: 
        model = Order
        fields = ['name', 'address', 'total', 'email']
        widgets = {
            'name':TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'address':TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'total':TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }

