from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """用户"""
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    image = models.ImageField(upload_to='user/%Y/%m', verbose_name='头像', max_length=200, default='images/icon/icon.png')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=12, verbose_name='性别', default='male')
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=50, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片', max_length=100)
    url = models.CharField(max_length=100, verbose_name='跳转地址')
    index = models.IntegerField(default=0, verbose_name='优先级')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FriendWeb(models.Model):
    """友链"""
    title = models.CharField(max_length=10, verbose_name='友链')
    url = models.CharField(max_length=100, verbose_name='跳转地址')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

