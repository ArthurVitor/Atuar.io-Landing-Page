from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')


def about(request):
    return render(request, 'paginas/sobre.html')


def services(request):
    return render(request, 'paginas/servicos.html')


def prices(request):
    return render(request, 'paginas/precos.html')


def blog(request):
    return render(request, 'paginas/blog.html')


def detail(request):
    return render(request, 'paginas/details.html')