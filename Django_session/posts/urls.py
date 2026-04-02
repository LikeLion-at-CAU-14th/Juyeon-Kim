from django.urls import path
from posts.views import *

urlpatterns = [
    # path('<int:id>', get_post_detail),

    path('', post_list, name = "post_list"), # Post 생성
    path('<int:post_id>/', post_detail, name = "post_detail"), # Post 단일조회, 수정, 삭제
    path('<int:post_id>/comments/',comment_list,name="comment_list"), #댓글 조회 
    path('<int:category_id>/posts/',postcategory_list,name="postcategory_list") # 카테고리 별 게시글 조회
]