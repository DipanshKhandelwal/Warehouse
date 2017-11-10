from django.shortcuts import render
from basic.models import Item


# Create your views here.
def more(request):
    if request.method == 'POST':
        string = request.POST['itemform']
        for i in Item.objects.all():
            if string == i.name:
                item = i
        return render(request, 'more/more.html', {'Items': Item.objects.all(), 'item': item})
    else:
        return render(request, 'more/more.html', {'Items': Item.objects.all()})
