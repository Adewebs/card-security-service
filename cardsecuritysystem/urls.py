from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('sample/', views.samplepage, name='sample'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.loginepage, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.register_parent, name='signup'),
    path('loggoff/', views.loggoff_parent, name='loggoff'),
    path('dashboard/', views.parents_dashboard, name='dashboard'),
path('generate/', views.generate_and_save_qr_images, name='generate'),
path('verification/<int:pk>/', views.verificationLink, name='verification'),
path('updatepicker/', views.pickerUpdate, name='updatepicker'),
]