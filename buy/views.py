from django.shortcuts import render, redirect
from basic.models import Item, Stock
import datetime

from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# Create your views here.
def buy(request):
    items = Item.objects.all()
    my_list = {}
    for i in items:
        total = 0
        for s in Stock.objects.filter(item=i):
            total += s.quantity
        my_list.setdefault(i.name, total)
    return render(request, 'buy/buy.html', {'dict': my_list, 'items': items})


def write_pdf(request):

    now = datetime.datetime.now()
    name = 'Statistics' + now.strftime("%d-%m-%Y") + '.pdf'
    doc = SimpleDocTemplate(name, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                            bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []

    data = [
        ["<b>S.No.</b>", "<b>Item</b>", "<b>Price</b>", "<b>Quantity</b>"],
    ]

    items = Item.objects.all()
    n = 0
    for i in items:
        total = 0
        n += 1
        for s in Stock.objects.filter(item=i):
            total += s.quantity
        data.append([str(n), str(i.name), str(i.price), str(total)])

    # TODO: Get this line right instead of just copying it from the docs
    style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                        ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                        ('VALIGN', (0, 0), (0, -1), 'TOP'),
                        ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                        ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                        ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                        ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                        ])

    # Configure style and word wrap
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in data]
    t = Table(data2)
    t.setStyle(style)

    ptext = '<font size=40>ANNADAATA FOOD CO.OP </font>'
    elements.append(Paragraph(ptext, s))
    elements.append(Spacer(1, 20))

    ptext = '<font size=20>Statistics on %s</font>' % (now.strftime("%d-%m-%Y"))
    elements.append(Paragraph(ptext, s))
    elements.append(Spacer(1, 20))

    elements.append(t)

    # Send the data and build the file
    doc.build(elements)

    return redirect('/buy')
