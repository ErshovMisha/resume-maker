from django.urls import path
from myapp1.views import index_page
from myapp1.views import login_view
from myapp1.views import generate_pdf
from myapp1.views import show_files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index_page),
    path('login/', login_view, name='login'),
    path("pd", show_files)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

