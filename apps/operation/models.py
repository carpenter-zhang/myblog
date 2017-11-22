from datetime import datetime

from django.db import models

from users.models import UserProfile
from acticle.models import Article


class Message(models.Model):
    """对网站留言"""
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name='留言用户')
    email = models.EmailField(verbose_name='邮箱')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class Publish(models.Model):
    """用户发表文章"""
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name='发表用户')
    article = models.ForeignKey(Article, null=True, blank=True, verbose_name='文章')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '发表文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}-to-{1}".format(self.user.username, self.article.name)


class Comment(models.Model):
    """用户对文章进行评论"""
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name='评论用户')
    article = models.ForeignKey(Article, null=True, blank=True, verbose_name='被评论文章')
    content = models.TextField(verbose_name='内容', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}-to-{1}".format(self.user.username, self.article.name)


class UserFav(models.Model):
    """收藏"""
    user = models.ForeignKey(UserProfile, verbose_name='收藏用户')
    article = models.ForeignKey(Article, verbose_name='被收藏文章')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}-to-{1}".format(self.user.username, self.article.name)
