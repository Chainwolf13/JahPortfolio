from django.shortcuts import render


# Create your views here.
def view_home(request):
    return render(request, 'index.html')


def view_ticketmaster(request):
    return render(request, 'ticketmaster.html')


def view_cpu(request):
    return render(request, 'Gor-3300k.html')


def view_ascendedking(request):
    return render(request, 'AscendedKing.html')


def view_simple_math_pro(request):
    return render(request, 'Jah_Simple_math_pro.html')


def contact(request):
    return render(request, 'Contact.html')