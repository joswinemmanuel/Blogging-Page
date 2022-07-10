from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="posts"),
    path("about/", views.about, name="about"),
    path("<slug:slug>/", views.post, name="post"),
]
