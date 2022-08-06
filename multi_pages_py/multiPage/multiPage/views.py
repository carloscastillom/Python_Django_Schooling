from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def contact(request):
    user_input = request.GET["user_input"]
    return render(request, 'contact.html')