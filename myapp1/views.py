from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TextInputForm
from .forms import ExampleForm
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from xhtml2pdf import pisa
from .models import Res_Input
from django.contrib import messages


def create_resume(request):
    if request.method == "POST":
        form = Res_Input(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  # призначаємо поточного користувача
            resume.save()
            return redirect('success_page')  # перенаправлення після успішного збереження
    else:
        form = Res_Input()
    return render(request, 'create_resume.html', {'form': form})


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
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('')
                else:
                    return HttpResponse('Disabled account')
            else:
                user = User.objects.create_user(username=cd['username'], password=cd['password'])
                user = authenticate(username=cd['username'], password=cd['password'])
                login(request, user)
                return redirect('')
    else:
        form = ExampleForm()
    return render(request, 'login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('')


def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        email1 = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(email=email1).exists():
                messages.info(request,'Emailal ready exists')
                return redirect('register')
            elif User.objects.filter(username=username1).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username1, email=email1, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

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
