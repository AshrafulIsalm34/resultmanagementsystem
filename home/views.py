from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')  
    else:
        return render(request, 'accounts/login.html') 