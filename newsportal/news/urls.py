from django.urls import path
# from django.urls.resolvers import URLPattern
from django.urls import path
from .views import PostList, PostDetail, PostCreate

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    # path('post/', PostDetail.as_view(), name='post'),
]
