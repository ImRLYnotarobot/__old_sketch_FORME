from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogsList.as_view(), name='blogs_list_url'),
    path('blog/<int:id>/', views.BlogDetail.as_view(), name='blog_detail_url'),
    path('blog/topic/<int:id>/', views.TopicDetail.as_view(), name='topic_detail_url'),
    path('blog/topic/create/', views.TopicCreate.as_view(), name='topic_create_url'),
    path('blog/topic/<int:id>/update/', views.TopicUpdate.as_view(), name='topic_update_url'),
    path('blog/topic/<int:id>/delete/', views.TopicDelete.as_view(), name='topic_delete_url'),
    path('test/', views.test),
    path('test/form/', views.MyForm.as_view(), name='test_form_url'),
    path('tags/', views.TagsList.as_view(), name='tags_list_url'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug:slug>/', views.TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<slug:slug>/update/', views.TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<slug:slug>/delete/', views.TagDelete.as_view(), name='tag_delete_url'),

]
