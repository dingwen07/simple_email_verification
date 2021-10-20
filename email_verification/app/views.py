from django.shortcuts import render
from django.http import HttpResponse

from .app import send_email
from .app_config import HomeConfig

def home(request):
    context = HomeConfig.CONTEXT
    return render(request, 'home.html', context)

def submit(request):
    email = request.POST.get('email')
    print(email)
    send_email(email, 'Test Message', f'Test Email sent to {email}')

    return HttpResponse('Submit')
