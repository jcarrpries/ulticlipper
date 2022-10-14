from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from backend.sync_view import SyncUpload, SyncChooseGame, SyncCommit

urlpatterns = [
    path('sync/upload/', SyncUpload.as_view()),
    path('sync/choosegame/', SyncChooseGame.as_view()),
    path('sync/commit/', SyncCommit.as_view()),
    path('testimport/', views.TestStatsImport.as_view()),
    path('clips/', views.ClipList.as_view()),
    path('clips/<int:pk>/', views.ClipDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
