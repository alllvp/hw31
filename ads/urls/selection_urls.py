from django.urls import path

from ads.views import SelectionUpdateView, SelectionListView, SelectionDeleteView, SelectionDetailView, SelectionCreateView

urlpatterns = [
    path('', SelectionListView.as_view(), name='all'),
    path('<int:pk>/', SelectionDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', SelectionUpdateView.as_view()),
    path('create/', SelectionCreateView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view()),
]