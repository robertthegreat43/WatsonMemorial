from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.contrib import admin, auth
from django.urls import path, include
from . import views, api_views
# camera_app/urls.py
from django.urls import path
from .views import video_feed
from .api_views import start_recording, stop_recording, list_recordings, download_video






urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('items/', views.items_list, name="items_list"),
    path('accounts/profile/', views.profile, name='profile'),
    path('index/', views.index, name="index"),
    path('Videorecording/', views.video, name='videorecording'),
    path('daily_bread/',views.daily_bread,name='daily_bread'),
    path('prayers_for_those_in_need/',views.prayers_for_those_in_need,name='prayers_for_those_in_need'),
    path('logged_out/', views.logged_out, name='logout'),
    path("accounts/", include(("django.contrib.auth.urls", "auth"),namespace="accounts")),
    path("accounts/password_reset/done/",auth.views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("accounts/reset/done/", auth.views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
    path('api/all_events/', api_views.EventsList.as_view(), name="all_events"),
    path('video_feed/', video_feed),
    path('api/start_recording/', start_recording),
    path('api/stop_recording/', stop_recording),
    path('api/videos/', list_recordings),
    path('api/download/<str:filename>/', download_video, name='download_video'),
    path('api/biblechat/', views.biblechat_api, name='biblechat_api'),
    path('biblechat/', views.biblechat, name='biblechat'),





]