from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('sign_in/', views.user_login, name='signin'),
    path('sign_up/', views.user_register, name='signup'),
    path('manage/', views.user_manage, name='userManage'),
    path('manage/post_del_user/', views.remove_user, name='userRemove'),
    path('manage/post_H_del_user/', views.restore_user, name='userRestore'),
    path('manage/get_query_user_info/', views.pull_query_user_info, name='getUserInfo'),
    path('manage/post_update_user_info/', views.update_user, name='postUserInfo'),
]