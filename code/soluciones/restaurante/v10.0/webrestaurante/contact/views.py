from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from contact.forms import ContactForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
            # Otra manera de obtener los datos del formulario
            # email = form.cleaned_data['email']
            # if 'gmail.com' in email:
            #     return HttpResponseRedirect(reverse_lazy('contact:thanks'))
            # else:
            #     form.add_error('email', 'dominio inválido')
    else:  # Método get
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def thanks(request):
    return render(request, 'contact/thanks.html')

@require_http_methods(['GET'])
def get_countries(request):
    countries = ['México', 'USA', 'Canada']
    return  JsonResponse({'countries':countries})    