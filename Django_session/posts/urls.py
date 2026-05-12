from django.contrib import admin
from django.urls import path, include
from posts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    # path('<int:id>', get_post_detail),

    # path('', post_list, name = "post_list"), # Post 생성
    # path('<int:post_id>/', post_detail, name = "post_detail"), # Post 단일조회, 수정, 삭제
    # path('<int:post_id>/comments/',comment_list,name="comment_list"), #댓글 조회 
    path('', PostList.as_view()),
    path('<int:post_id>/', PostDetail.as_view()),
    path('<int:post_id>/comment/', CommentList.as_view()),
    path('<int:post_id>/comment/<int:comment_id>/', CommentDetail.as_view()),


    # 토큰 관련 url 추가
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]