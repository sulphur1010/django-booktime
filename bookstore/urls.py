from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='bookstore'

urlpatterns = [
    path('',views.BookListView.as_view(),name='home'),
    path('details/<str:title>/',views.book_details,name='details'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('register',views.signUpView,name='register'),
]