from django.urls import path

from users.views import ProfileView, UsersSearchView

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('search', UsersSearchView.as_view()),
]
