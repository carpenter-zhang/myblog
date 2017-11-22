import xadmin
from xadmin import views
from .models import UserProfile, Banner, FriendWeb


# class UserProfileAdmin(object):
#     list_display = ['username']


class BannerAdmin(object):
    list_display = ['title', 'index']
    search_fields = ['title']
    list_filter = ['title', 'index']


class FriendWebAdmin(object):
    list_display = ['title', 'url']
    search_fields = ['title']
    list_filter = ['title']


class GlobalSetting(object):
    site_title = 'myblog'
    site_footer = 'myblog'
    menu_style = 'accordion'


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(FriendWeb, FriendWebAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)

