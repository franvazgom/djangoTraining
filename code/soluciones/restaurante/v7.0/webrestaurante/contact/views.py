from django.shortcuts import render
from django.http import HttpResponseRedirect
from contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            print(f'Datos del formulario {name}')
            return HttpResponseRedirect('/')  # Home
        else:
            errors = form.errors
            return render(request, 'contact/contact.html', {'form': form, 'errors': errors})
    else:  # Método get
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
