from django.shortcuts import render


def home(request):
    # context = {'name'}
    return render(request, "main/home.html")
