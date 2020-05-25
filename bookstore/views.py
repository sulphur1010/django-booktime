from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class BookListView(ListView):
    template_name='bookstore/index.html'
    model=Book
    paginate_by=6
    # context_object_name='books'



def book_details(request,title):
    book=Book.objects.get(title=title)
    context={
        'book':book
    }

    return render(request,'bookstore/book_detail.html',context)


def loginView(request):
    form=AuthenticationForm()

    context={
        'form':form
    }
    return render(request,'bookstore/login.html',context)


def signUpView(request):
    form=UserRegisterForm()

    if request.method=='POST':
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

    context={
        'form':form
    }
    return render(request,'bookstore/register.html',context)