from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from contact.forms import ContactForm

# return HttpResponseRedirect('/contact/thanks') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse_lazy('contact:thanks')) 
    else:  # Método get
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             print(f'Datos del formulario {name}')
#             email = form.cleaned_data['email']
#             if 'gmail.com' in email: 
#                 return HttpResponseRedirect(reverse_lazy('contact:thanks')) 
#             else:
#                 form.add_error('email', 'Dominio inválido')
#     else:  # Método get
#         form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': form})

def thanks(request):
    return render(request, 'contact/thanks.html')