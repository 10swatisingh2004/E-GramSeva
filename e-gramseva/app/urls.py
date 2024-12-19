from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home1,name="home1"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>/update/', views.update_service, name='update_service'), 
    path('service/<int:service_id>/delete/', views.delete_service, name='delete_service'),
    path('services/apply/<int:service_id>/', views.apply_service, name='apply_service'),
    path('staff/applications/update/<int:application_id>/', views.update_application_status, name='update_application_status'),

    path('applications/', views.my_applications, name='my_applications'),
    path('create-serivces/', views.create_service, name='create_service'),
    path('staff/applications/', views.staff_applications, name='staff_applications'),
]
