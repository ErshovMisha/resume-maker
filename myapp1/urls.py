from django.urls import path
from myapp1.views import index_page
from myapp1.views import login_view
from myapp1.views import generate_pdf

urlpatterns = [
    path("", index_page),
    path('login/', login_view, name='login'),
    path("pd", generate_pdf)
]

