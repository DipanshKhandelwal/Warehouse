from django.shortcuts import render, HttpResponse
import os


# Create your views here.
def sell(request):
    my_list = []
    for file in os.listdir("buy/static/pdf/"):
        if file.endswith(".pdf"):
            file = file[:len(file)-4]
            my_list.append(file)
    return render(request, 'sell/sell.html', {'go': my_list})


def open_pdf(request, slug):
    with open('buy/static/pdf/'+slug+'.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename='+slug+'.pdf'
        return response
