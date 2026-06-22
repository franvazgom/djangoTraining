from django.forms import ModelForm, TextInput, Textarea
from services.models import Service
from django_ckeditor_5.widgets import CKEditor5Widget


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'sub_title', 'content', 'image',]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'sub_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub título'}),
            'content': CKEditor5Widget(config_name='extends'),
        }
