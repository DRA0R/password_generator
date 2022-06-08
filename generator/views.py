from django.shortcuts import render
import random
#from django.http import HttpResponse

# def about(request):
#     return HttpResponse('Hello, world!')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    character = list('abcdefghijklmnopqrstvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()-+_='))

    if request.GET.get('numbers'):
        character.extend(list('123456789'))

    for x in range(length):
        generated_password += random.choice(character)


    return render(request, 'password.html', {
        'password':generated_password
    })