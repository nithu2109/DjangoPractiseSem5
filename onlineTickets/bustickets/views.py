from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
from .models import BusDetails
from .forms import Ticket
# Create your views here.
def home(request):
    form1=BusDetails.objects.all()
    form=Ticket()
    if(request.method=='POST'):
        form=Ticket(request.POST)
        if form.is_valid():
            Bus_No = form.cleaned_data["Bus_No"]
            No_of_Persons = form.cleaned_data["No_of_Persons"]
            nit = models.BusDetails.objects.filter(Bus_No=Bus_No)
             
            if nit.exists():
                s = models.BusDetails.objects.get(Bus_No=Bus_No)
                if s.Destinations == form.cleaned_data["Destinations"]:
                    if s.Seats_Available >= No_of_Persons:
                        s.Seats_Available = s.Seats_Available - No_of_Persons
                        s.save()
                        cost = No_of_Persons * s.TicketCosts
                        return render(
                            request,
                            "bustickets/index.html",
                            {
                                "error": "Booked successfully",
                                "cost": cost,
                                "form": forms.Ticket(),
                                'form1':form1

                            },
                        )
                    else:
                        return render(
                            request,
                            "bustickets/index.html",
                            {
                                "error": "No seats available",
                                "form": forms.Ticket(),
                                'form1':form1
                            },
                        )
                else:
                    return render(
                        request,
                        "bustickets/index.html",
                        {
                            "form": form,
                            "error": "Wrong Destinations",
                            'form1':form1
                        },
                    )
            else:
                return render(
                    request,
                    "bustickets/index.html",
                    {
                        "form": form,
                        "error": "Invalid busnumber",
                        'form1':form1
                    },
                )
    return render(request,"bustickets/index.html",context={'form':form,'form1':form1})

# def main(request):
#     return HttpResponse("Hello, world!")