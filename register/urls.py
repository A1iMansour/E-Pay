
from . import views
from django.urls import path

urlpatterns = [
   
    path('',views.home, name='homefunc'),
    path('about/' ,views.about, name='aboutfunc'),
    path('login/', views.loginf, name='loginfunc'),
    path('signup/', views.signup , name='signupfunc'),
    path('logout/', views.userlogout, name='logout'),
    path('registeradmin/', views.register_admin, name='register_admin'),
]