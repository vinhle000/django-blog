from django.contrib.auth.models import User
from blogging.models import Post, Category
from rest_framework import serializers, permissions


""" requests.get("http://fierce-crag-38242.herokuapp.com/api/posts/").json()
    {'count': 3, 'next': None, 'previous': None, 'results':
     [
     {'url': 'http://127.0.0.1:8000/api/posts/1/', 
     'title': 'Dogs', 'text': 'R', 'created_date': '2020-05-22T04:05:40.727989Z',
     'modified_date': '2020-05-22T04:05:40.727989Z', 'published_date': None,
      'author': 'http://127.0.0.1:8000/api/users/1/'}, """


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'text', 'created_date', 'modified_date', 'published_date', 'author']



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description', 'posts']
