from django.shortcuts import render, HttpResponse


def home(request):
    # return HttpResponse("<H1> Mi página </H1>" +
    #                     "<H2> Aquí va la página </H2>")
    return render(request, 'core/home.html')
