from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Employee Management System")


def emp_post(request):
    form = forms.emp_form()
    if request.method == "POST":
        form = forms.emp_form(request.POST)
        if form.is_valid():
            # write data to csvfile
            f = open("employee.csv", "a")
            f.write(
                form.cleaned_data["ename"]
                + ","
                + form.cleaned_data["eaddress"]
                + ","
                + str(form.cleaned_data["ejoin_dt"])
                + ","
                + form.cleaned_data["edept"]
                + "\n"
            )
            f.close()
            form.save(commit=True)
            return emp_archive(request)
    return render(request, "emp_form.html", {"form": form})


def emp_archive(request):
    s = models.emploee_details.objects.all()
    form = forms.emp_form()
    return render(request, "emp_form.html", {"s": s, "form": form})
