from django.shortcuts import render, redirect
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Article, Catagory
from operation.models import Publish, Comment, UserFav
from utils.mixin_utils import get_date, get_weekday, get_fav_articles, get_new_message


class ArticleListView(View):
    """文章列表"""
    def get(self, request):
        all_articles = Article.objects.all().order_by('-add_time')

        filters = request.GET.get('filter', '')
        if filters == 'front':
            all_articles = all_articles.filter(column__name='前端')
        elif filters == 'back':
            all_articles = all_articles.filter(column__name='后端')

        tags = request.GET.get('tag', '')
        if tags != '':
            all_articles = all_articles.filter(tags__name=tags)

        fav = request.GET.get('fav', '')
        if fav == 'true':
            all_articles = Article.objects.filter(userfav__user=request.user)

        keywords = request.GET.get('keywords', '')
        if keywords != '':
            all_articles = Article.objects.filter(Q(tags__name__icontains=keywords) | Q(name__icontains=keywords) |
                                                  Q(brief__icontains=keywords) | Q(content__icontains=keywords))

            all_articles = list(set(all_articles))


        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 7, request=request)
        articles = p.page(page)

        fav_articles = get_fav_articles()
        date = get_date()
        weekday = get_weekday()
        new_message = get_new_message()

        context = {'date': date, 'weekday': weekday,
                   'fav_articles': fav_articles, 'articles': articles, 'new_message': new_message}
        return render(request, 'list.html', context)


class ArticleInfo(View):
    """文章详情页"""
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        # publish = article.publish_set.all()
        # if publish is None:
        #     # 草稿
        #     return redirect('/')
        # publish = publish[0]

        # 阅读人数
        if request.user.is_authenticated():
            article.see_num += 1
        else:
            article.see_unkown_num += 1
        article.save()

        # 标签
        tags = article.tags.all()

        # 相关推荐
        relate_articles = Article.objects.filter(tags__name=tags[0].name)
        if len(relate_articles) > 8:
            relate_articles = relate_articles[:8]

        # 用户评论
        comments = Comment.objects.filter(article=article).order_by('-add_time')

        fav_articles = get_fav_articles()
        new_message = get_new_message()
        date = get_date()
        weekday = get_weekday()
        context = {'article': article, 'tags': tags, 'relate_articles': relate_articles,
                   'date': date, 'weekday': weekday, 'fav_articles': fav_articles, 'new_message': new_message,
                   'comments': comments}
        return render(request, 'content.html', context)


class AddComment(View):
    def post(self, request):
        user = request.user
        article_id = request.POST.get('article_id', '')
        content = request.POST.get('content', '')
        if content == '':
            return HttpResponse("{'status': 'fail', 'msg': 'no content'}", content_type='application/json')

        article = Article.objects.get(id=int(article_id))

        comment = Comment()
        comment.user = user
        comment.article = article
        comment.content = content
        comment.save()

        return HttpResponse("{'status': 'success'}", content_type='application/json')
