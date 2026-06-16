from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from contact.forms import ContactForm


def contact(request):
    errors = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            
            return HttpResponseRedirect(reverse_lazy('contact:thanks')) 
        else:
            errors = form.errors            
    else:  # Método get
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'errors': errors})

def thanks(request):
    return render(request, 'contact/thanks.html')
