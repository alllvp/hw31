from django.urls import path

from ads.views import CategoryView, CategoryDetailView
from users.views import UserCreateView, UserListView

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
]
