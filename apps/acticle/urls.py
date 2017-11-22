from django.conf.urls import url

from .views import ArticleInfo, ArticleListView, AddComment

urlpatterns = [
    url(r'^(?P<article_id>\d+)/$', ArticleInfo.as_view(), name='article_info'),

    url(r'^list/$', ArticleListView.as_view(), name='article_list'),

    url(r'^add_comment/$', AddComment.as_view(), name='add_comment'),

    url(r'^fav/', ArticleListView.as_view(), name='fav'),

]