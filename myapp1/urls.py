from django.urls import path
from myapp1.views import index_page

urlpatterns = [
    path("", index_page)
]