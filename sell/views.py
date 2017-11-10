from django.shortcuts import render
import os


# Create your views here.
def sell(request):
    my_list = []
    for file in os.listdir("buy/static/pdf/"):
        if file.endswith(".pdf"):
            file = file[:len(file)-4]
            my_list.append(file)
    return render(request, 'sell/sell.html', {'go': my_list})
