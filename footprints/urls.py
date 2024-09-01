from django.urls import path

# Create your urls here
from .views import VisitGetView, VisitPostView, VisitPicsGetView, VisitPicsPostView, TaggedFootstepsGetView

appname = "footprints"

urlpatterns = [
    path("visit/", VisitGetView.as_view(), name="visit_get"),
    path("visit/post/", VisitPostView.as_view(), name="visit_post"),
    path("visit_pics/", VisitPicsGetView.as_view(), name="pics_get"),
    path("visit_pics/post/", VisitPicsPostView.as_view(), name="pics_post"),
    path("tagged_visits/", TaggedFootstepsGetView.as_view(), name="tagged_visits")
]