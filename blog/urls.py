"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from .settings import MEDIA_ROOT, STATIC_ROOT
from django.views.static import serve

from users.views import IndexView, LoginView, RegisterView, LogoutView, AboutView, FriendView, \
    PersonView, AddMessage, UploadImageView, UpdatePwdView, UpdateEmailView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)', serve, {'document_root': STATIC_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 登录等相关
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 首页不重要
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^friend/', FriendView.as_view(), name='friend'),

    # 个人资料
    url(r'^person/', PersonView.as_view(), name='person'),
    url(r'^upload_image/$', UploadImageView.as_view(), name='upload_image'),
    url(r'^update_pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),

    url(r'^add_message/$', AddMessage.as_view(), name='add_message'),

    url(r'^article/', include('acticle.urls', namespace='article'))
]

handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
handler403 = 'users.views.permission_denied'
