from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'fiufhlsiufkhwf'})

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=.,'))

    length = int(request.GET.get('length', 12))

    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator/password.html', { 'password':thePassword })

def about(request):
    return render(request, 'generator/about.html')
