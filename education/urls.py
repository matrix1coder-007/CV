from django.urls import path

# Create your urls here
from .views import SchoolGetView, SchoolPostView, CollegeGetView, CollegePostView

appname = "education"

urlpatterns = [
    path("schools/", SchoolGetView.as_view(), name="school_get"),
    path("school_post/", SchoolPostView.as_view(), name="school_post"),
    path("colleges/", CollegeGetView.as_view(), name="college_get"),
    path("college_post/", CollegePostView.as_view(), name="college_post"),
]
