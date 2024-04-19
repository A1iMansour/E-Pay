from django.shortcuts import render
from .models import me, Usermoney
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

# Create your views here.
def home(request):
    #context={ 
        #'people': me.objects.all()
        #}
    return render(request,'home.html' )

def about(request):
    return render(request,'about.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            currency = form.cleaned_data['currency']
            Usermoney.objects.create(user=user, currency=currency, balance=100)
            login(request, user)
            messages.success(request, 'Your account was created successfully!')
            return redirect('homefunc')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginf(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homefunc')
            else:
                #handling invalid login credentials
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

