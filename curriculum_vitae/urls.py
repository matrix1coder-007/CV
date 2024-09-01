"""curriculum_vitae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    # call the achievements app urls file appending after their key
    path('achievements/', include("achievements.urls")),
    # call the blogs app urls file appending after their key
    path('blogs/', include("blogs.urls")),
    # call the projects app urls file appending after their key
    path('contacts/', include("contacts.urls")),
    # call the education app urls file appending after their key
    path('education/', include("education.urls")),
    # call the footsteps app urls file appending after their key
    path('footprints/', include("footprints.urls")),
    # call the projects app urls file appending after their key
    path('projects/', include("projects.urls")),
    # call the work_experience app urls file appending after their key
    path('work_experience/', include("work_experience.urls")),
]
