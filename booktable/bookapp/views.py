from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .forms import Book_form

# Create your views here.

def bookinfo(request):
    form = Book_form()
    if request.method == "POST":
        form = Book_form(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('./display')
    return render(request, 'formapp/insert.html', context={'form': form})

