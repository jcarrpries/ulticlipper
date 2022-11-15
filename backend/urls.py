from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from backend.sync_view import SyncUpload, SyncChooseGame, SyncCommit

urlpatterns = [
    path('sync/upload/', SyncUpload.as_view()),
    path('sync/choosegame/', SyncChooseGame.as_view()),
    path('sync/commit/', SyncCommit.as_view()),

    path('clips/', views.ClipList.as_view()),
    path('clips/<int:pk>/', views.ClipDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>/', views.TagDetail.as_view()),
	path('tag_groups/', views.TagGroupList.as_view()),
    path('tag_groups/<int:pk>/', views.TagGroupDetail.as_view()),

    path('clips_by_video/<int:pk>/', views.ClipsByVideo.as_view()),

    path('healthcheck/', views.HealthCheck.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
