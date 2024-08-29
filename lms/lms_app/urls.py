from django.urls import path
from . import views
# why dott . -> urls جمب ال views لان ال
urlpatterns = [
    path('',views.index, name='index'),
    path('books',views.books, name='books'),
    path('update<int:id>',views.update, name='update') ,
    path('delete<int:id>',views.delete, name='delete') ,
]