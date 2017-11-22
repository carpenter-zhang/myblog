from datetime import datetime
from django.db import models

from DjangoUeditor.models import UEditorField


class Catagory(models.Model):
    """文章所属的类型"""
    name = models.CharField(max_length=20, verbose_name='栏目')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=20, verbose_name='标签名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章"""
    column = models.ForeignKey(Catagory, verbose_name='栏目')
    tags = models.ManyToManyField(Tag, verbose_name='标签', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='标题')
    brief = models.CharField(max_length=500, verbose_name='简介', default='')
    image = models.ImageField(upload_to='content/', verbose_name='图片')
    resouce = models.CharField(max_length=20, verbose_name='来源')
    see_num = models.IntegerField(default=1, verbose_name='阅读人数')
    see_unkown_num = models.IntegerField(default=0, verbose_name='未登录查看人数')
    content = UEditorField(verbose_name='内容', imagePath='content/ueditor/', width=1000, height=400,
                              filePath='content/ueditor/', default='')
    fav_nums = models.IntegerField(default=0, verbose_name='点赞数')
    tag = models.CharField(max_length=20, verbose_name='课程标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

