from django.shortcuts import render, HttpResponse


# def home(request):
#     return HttpResponse("""
#                         <H1> Hola Mundo!!! </H1>
#                         <H2> Bienvenidos a mi página </H2>
#                         """)

def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')
