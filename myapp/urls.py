from django.urls import path
from myapp import views



urlpatterns = [
    path('', views.index, name='home'),
    path('add-employee', views.add_employee, name='add_employee'),
    path('details/<int:pk>', views.details, name='details'),
    path('update/<int:pk>', views.update, name='update'),
    path('management/', views.management, name='management'),
]   