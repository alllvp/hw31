from django.urls import path

from ads.views import AdListView, AdDetailView, AdCreateView, AdUploadImageView, AdUpdateView, AdDeleteView

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
]
