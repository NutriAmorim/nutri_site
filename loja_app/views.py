from django.shortcuts import render

def home(request):
    print("A view home foi chamada!")
    return render(request, 'loja_app/home.html')