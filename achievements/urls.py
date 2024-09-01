from django.urls import path

# Create your urls here
from .views import MeritGetView, MeritPostView

appname = "achievements"

urlpatterns = [
    path("", MeritGetView.as_view(), name="merit_get"),
    path("post/", MeritPostView.as_view(), name="merit_post"),
]