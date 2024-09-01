from django.urls import path

# Create your urls here
from .views import ContactGetView, ContactPostView

appname = "contacts"

urlpatterns = [
    path("", ContactGetView.as_view(), name="contact_get"),
    path("post/", ContactPostView.as_view(), name="contact_post"),
]