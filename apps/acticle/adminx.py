import xadmin

from .models import Catagory, Article, Tag


class CatagoryAdmin(object):
    list_display = ['name', 'id']
    search_fields = ['name', 'id']
    list_filter = ['name', 'id']


class TagAdmin(object):
    list_display = ['name', 'id']
    search_fields = ['name', 'id']
    list_filter = ['name', 'id']


class ArticleAdmin(object):
    list_display = ['name', 'column', 'see_num']
    search_fields = ['name', 'column', 'see_num']
    list_filter = ['name', 'column', 'see_num']
    style_fields = {'content': 'ueditor'}

xadmin.site.register(Catagory, CatagoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag, TagAdmin)
