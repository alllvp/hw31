from django.urls import path

from ads.views import CategoryView, CategoryDetailView, CategoryDeleteView, CategoryCreateView, CategoryUpdateView

urlpatterns = [
    path('', CategoryView.as_view(), name='all_categories'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='cat_detail'),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]
