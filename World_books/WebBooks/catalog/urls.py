from django.urls import path
from .import views
from django.conf.urls import re_path as url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

# urlpatterns += [
#     url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
# ]
