from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm

def userInitialezed(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return HttpResponseRedirect('/success/')
    else:
        form = UserForm()

    return render(request, 'store.html', {'form': form})        