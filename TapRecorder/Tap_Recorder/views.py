from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import Tapes
from .forms import TapeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    context={
        'posts': None
    }
    return render(request,'Tap_Recorder/home.html', context)

def about(request):
    return render(request, 'Tap_Recorder/about.html',{'title':'About'})

@login_required
def upload_tape(request):
    if request.method == 'POST':
        form = TapeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title= form.cleaned_data.get('title')
            messages.success(request, f'{title} is added')
            return redirect(home)
    else:
        form = TapeForm()
        context = {'form': form}
        return render(request, 'Tap_Recorder/upload_tape.html', context)
