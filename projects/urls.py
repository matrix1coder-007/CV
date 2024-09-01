from django.urls import path

# Create your urls here
from .views import ProjectGetView, ProjectPostView

appname = "projects"

urlpatterns = [
    path("", ProjectGetView.as_view(), name="project_get"),
    path("post/", ProjectPostView.as_view(), name="project_post"),
]