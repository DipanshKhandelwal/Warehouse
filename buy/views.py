from django.shortcuts import render


# Create your views here.
def buy(request):
    return render(request, 'buy/buy.html')
