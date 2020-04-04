from django.shortcuts import render


def home(request):
    # context = {'name'}
    return render(request, "main/home.html")


def bio(request):
    return render(request, "main/bio.html")


def photos(request):
    return render(request, "main/photos.html")
