import xadmin
from .models import Message, Publish, Comment, UserFav


class MessageAdmin(object):
    list_display = ['user', 'add_time']
    search_field = ['user', 'add_time']
    list_filter = ['user', 'add_time']


class PublishAdmin(object):
    list_display = ['user', 'article', 'add_time']
    search_field = ['user', 'add_time']
    list_filter = ['user', 'add_time']


class CommentAdmin(object):
    list_display = ['user', 'add_time']
    search_field = ['user', 'add_time']
    list_filter = ['user', 'add_time']


class UserFavAdmin(object):
    list_display = ['user', 'add_time']
    search_field = ['user', 'add_time']
    list_filter = ['user', 'add_time']

xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Publish, PublishAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(UserFav, UserFavAdmin)
