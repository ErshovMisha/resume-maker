from django.urls import path, include
from myapp1.views import index_page
from myapp1.views import login_view
from myapp1.views import generate_pdf
from myapp1.views import logoutUser
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", index_page, name=''),
    path('login/', login_view, name='login'),
    path("pd/", generate_pdf),
    path('logout/', logoutUser, name='logout'),
    path('create-resume/', views.create_resume, name='create_resume'),
    # path('api-auth/', include('rest_framework.urls')),
    path('register',views.register,name='register')
]

