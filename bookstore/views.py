from django.shortcuts import render
from .models import Book
from django.views.generic import ListView


class BookListView(ListView):
    template_name='bookstore/index.html'
    model=Book
    paginate_by=3
    # context_object_name='books'



def book_details(request,title):
    book=Book.objects.objects.filter(title=title).first()
    context={
        'book':book
    }

    return render(request,'bookstore/book_detail.html')


