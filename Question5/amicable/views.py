from django.shortcuts import render

# Create your views here.
def home(request):
    pairs = [(150, 290), (220, 284), (1184, 1210), (1350, 1851)]
    dpairs = {}
    for x,y in pairs:
        dpairs[(x,y)] = isAmicable_pair(x, y)
    return render(request,"amicable/index.html",{'pairs':dpairs.items()})

def get_proper_divisors(n):
    divisors = [x for x in range(1, n) if n % x == 0]
    return divisors

def check_property(n):
    abundant_list = [x for x in range(2, n+1) if sum(get_proper_divisors(x)) > x]
    deficient_list = [x for x in range(2, n+1) if sum(get_proper_divisors(x)) < x]
    equal_list = [x for x in range(2, n+1) if sum(get_proper_divisors(x)) == x]
    return abundant_list, deficient_list, equal_list

def isAmicable_pair(x, y):
    div_x = get_proper_divisors(x)
    div_y = get_proper_divisors(y)
    sum_div_x = sum(div_x)
    sum_div_y = sum(div_y)
    if sum_div_x == y and sum_div_y == x:
        return "AMICABLE"
    else:
        return "NOT AMICABLE"
