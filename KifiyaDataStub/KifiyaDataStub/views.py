from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html', {'title': 'Welcome to My Kifiya Data Stub'})
