from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TextInputForm
from .forms import ExampleForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def index_page(request):
    # Логіка вашої сторінки index_page
    if request.method == "GET":
        form = TextInputForm()
    elif request.method == "POST":
        form = TextInputForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'form': form})


def login_view(request):
    form = ExampleForm()
    return render(request, 'login.html', {'form': form})


def generate_pdf(request):
    if request.method == 'POST':
        # Отримайте HTML-шаблон
        template = get_template('template1.html')
        html = template.render()

        # Створіть PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="res.pdf"'

        # Створення PDF з HTML
        pisa.CreatePDF(html, dest=response)

        return response
    return render(request, 'template1.html')

