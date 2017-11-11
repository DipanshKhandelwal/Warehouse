from django.shortcuts import render
from basic.models import Stock, Item, Farmer
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def store(request):
    my_list = {}
    for i in Item.objects.all():
        total = 0
        for s in Stock.objects.filter(item=i, master=request.user):
            total += s.quantity
            my_list.setdefault(i.name, total)

        my_list2 = Stock.objects.filter(master=request.user)
    farmer = Farmer.objects.filter(user=request.user)
    return render(request, 'store/store.html', {'dict': my_list, 'dict2': my_list2, 'Farmer': farmer})
