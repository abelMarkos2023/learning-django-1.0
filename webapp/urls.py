from django.urls import path

from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.loginView,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create_record',views.create_record,name='create_record'),
    path('update_record/<int:pk>',views.update_record,name='update_record'),
    path('view_record/<int:pk>',views.view_record,name='view_record'),
    path('logout',views.logout,name='logout')
]