from django.urls import path, include
from blogging.views import stub_view
from blogging.views import list_view, detail_view
from rest_framework import routers



urlpatterns = [
    path("", list_view, name="blog_index"),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
]
