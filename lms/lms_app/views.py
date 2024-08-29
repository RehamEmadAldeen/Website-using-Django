from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.
#  فهو كده بقى شايفة settings في ال templates عشان بالفعل كتبت كلمة templates\demo.html هنا معملتش 


def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cayegory = CategoryForm(request.POST)
        if add_cayegory.is_valid():
            add_cayegory.save()


    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formCate': CategoryForm(),
        'allbooks': Book.objects.filter(active = True).count(),  # active = True -> available books
        'booksold': Book.objects.filter(status = 'sold').count(),  # active = True -> available books
        'bookavailable': Book.objects.filter(status = 'available').count(),  # active = True -> available books
        'bookrental': Book.objects.filter(status = 'rental').count(),  # active = True -> available books
    }
    return render(request, 'pages/index.html', context)


def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)




    context = {
        'category': Category.objects.all(),
        'books': search,
        'formCate': CategoryForm(),
    }
    return render(request, 'pages/books.html',context)


def update(request,id):
    # get the id of each book
    book_id = Book.objects.get(id = id)
# get(id = id) -> get(id in the function = id book)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/') # index page
    else:
        book_save = BookForm(instance=book_id)

    context = {
        'form': book_save,
    }
    return render(request, 'pages/update.html', context)


def delete(request,id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/') # / -> index page
    return render(request, 'pages/delete.html')
