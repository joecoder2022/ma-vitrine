from django.shortcuts import render
from .forms import SaveUser
from .models import User

# Create your views here.

def enregistrement(request):
    if request.method == 'POST':
        fm = SaveUser(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ms = fm.cleaned_data['message']
            sv = User(name = nm, email = em, message = ms)
            sv.save()
            fm = SaveUser()
    else:
        fm = SaveUser()
    return render(request,'facebook/enregistrement.html',{'form':fm})
