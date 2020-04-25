from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('choose_paper/', views.choosePaper, name='choose_paper'),
    path('display_page/1/', views.getPaperComment, name='display_page'),
    path('edit_comment/', views.editComment, name='edit_comment'),  # 进入添加评论的页面
    path('display_page/2/', views.postComment, name='post_comment'),  # 添加评论，返回display页面
    path('edit_reply/', views.editReply, name='edit_reply'),   # 进入添加回复的页面
    path('display_page/3/', views.postReply, name='post_reply'),  # 添加回复，返回display_page

]