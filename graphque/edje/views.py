from django.shortcuts import render
from .graph import Graph,g

# Create your views here.
def printGraph(request):
    return render(request, 'edje/index.html', {'e_list':g.sortEdges()})
