from django.shortcuts import render

# Create your views here.
def home(request):
    alist,dlist,elist=check_property(30)
    return render(request,'numbertheory/index.html',{'alist':alist, 'dlist':dlist, 'elist':elist})

def get_proper_divisors(n):
    divisors=[x for x in range(1,n) if n % x ==0 ]
    return divisors

def check_property(n):
    perfect_list=[x for x in range(2, n+1) if sum(get_proper_divisors(x)) == x]
    deficient_list=[x for x in range(2, n+1) if sum(get_proper_divisors(x)) < x]
    abundant_list=[x for x in range(2, n+1) if sum(get_proper_divisors(x)) > x]
    return perfect_list,deficient_list,abundant_list

