from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('testimport/', views.TestStatsImport.as_view()),
    path('clips/', views.TestClipList.as_view()),
    path('clips/<int:pk>/', views.TestClipDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
