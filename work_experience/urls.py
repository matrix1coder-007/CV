from django.urls import path

# Create your urls here
from .views import WorkExpGetView, WorkExpPostView

appname = "work_experience"

urlpatterns = [
    path("", WorkExpGetView.as_view(), name="workexp_get"),
    path("post/", WorkExpPostView.as_view(), name="workexp_post"),
]