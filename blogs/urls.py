from django.urls import path, re_path
from . import views

app_name = 'blogs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name = 'topic'),
    path('new_topics/', views.new_topic, name='new_topic'),
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name = 'new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name = 'edit_entry'),
]