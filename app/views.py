from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')


def sobre(request):
    return render(request, 'app/sobre.html')


def contato(request):
    return render(request, 'app/contato.html')
