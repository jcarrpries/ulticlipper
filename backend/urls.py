from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('clips/', views.ClipList.as_view()),
    path('clips/<int:pk>/', views.ClipDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
