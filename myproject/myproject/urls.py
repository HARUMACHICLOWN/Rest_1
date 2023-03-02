from django.urls import path

from django.contrib import admin

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('books/create/', views.book_create),
    path('books/update/<int:pk>/', views.book_update),
    path('books/delete/<int:pk>/', views.book_delete),
]
