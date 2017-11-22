import json

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.backends import ModelBackend
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import UserProfile, Banner, FriendWeb
from .forms import LoginForm, RegisterForm, UploadImageForm, UpdatePwdForm, UpdateUserInfoForm, UpdateEmailForm
from operation.models import Message
from acticle.models import Article
from utils.mixin_utils import get_fav_articles, get_date, get_weekday, get_new_message, LoginRequiredMixin


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    """首页"""
    def get(self, request):
        # 轮播图
        banners = Banner.objects.all().order_by('-index')[:3]

        # 热门排行:点赞人数
        hots_articles = Article.objects.all().order_by('-fav_nums')[:5]

        # 热门推荐:阅读人数
        fav_articles = get_fav_articles()

        # 最新文章
        new_articles = Article.objects.all().order_by('-add_time')[:8]

        # 获取日期
        date = get_date()
        weekday = get_weekday()
        new_message = get_new_message()

        context = {'banners': banners, 'hots_articles': hots_articles,
                   'fav_articles': fav_articles, 'new_articles': new_articles,
                   'date': date, 'weekday': weekday, 'new_message': new_message}
        return render(request, 'index.html', context)


class RegisterView(View):
    """注册"""
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'reg.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)
        # 表单验证
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        if UserProfile.objects.filter(Q(username=username) | Q(email=email)):
            context = {'register_form': register_form, 'msg': '用户已经存在'}
            return render(request, 'reg.html', context)

        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if register_form.is_valid() and password1 == password2:

            user = UserProfile()
            user.username = username
            user.email = request.POST.get('email', '')
            user.password = make_password(password1)
            user.save()

            return redirect('/')
            # return HttpResponseRedirect(reversed('login'))
        else:
            context = {'register_form': register_form, 'msg': '密码不一致'}
            return render(request, 'reg.html', context)


class LoginView(View):
    """登录"""
    def get(self, request):
        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # return HttpResponseRedirect(reversed('index'))
                return redirect('/')
            else:
                context = {'login_form': login_form, 'msg': '用户名或密码错误'}
                return render(request, 'login.html', context)

        return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AboutView(View):
    """关于我们"""
    def get(self, request):
        fav_articles = get_fav_articles()
        date = get_date()
        weekday = get_weekday()
        new_message = get_new_message()
        context = {'date': date, 'weekday': weekday, 'fav_articles': fav_articles, 'new_message': new_message}
        return render(request, 'about.html', context)


class AddMessage(View):
    """添加留言"""
    def post(self, request):
        user = request.POST.get('user', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')

        message = Message()
        user = UserProfile.objects.filter(username=user)
        if user:
            message.user = user[0]
        if request.user.is_authenticated():
            message.user = request.user

        message.email = email
        message.content = content
        message.save()
        return redirect('/about/')


class FriendView(View):
    """友情链接"""
    def get(self, request):
        friends = FriendWeb.objects.all()

        fav_articles = get_fav_articles()
        date = get_date()
        weekday = get_weekday()
        new_message = get_new_message()
        context = {'date': date, 'weekday': weekday, 'fav_articles': fav_articles, 'new_message': new_message,
                   'friends': friends}
        return render(request, 'friendly.html', context)


class PersonView(LoginRequiredMixin, View):
    """个人中心"""
    def get(self, request):
        update_email_form = UpdateEmailForm()
        context = {'update_email_form': update_email_form}
        return render(request, 'person.html', context)

    def post(self, request):
        """修改个人信息"""
        update_user_form = UpdateUserInfoForm(request.POST, instance=request.user)
        if update_user_form.is_valid():
            update_user_form.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        return HttpResponse(json.dumps(update_user_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    """修改头像"""
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        return HttpResponse("{'status': 'fail'}", content_type='application/json')


class UpdatePwdView(LoginRequiredMixin, View):
    """修改密码"""
    def post(self, request):
        update_pwd_form = UpdatePwdForm(request.POST)
        if update_pwd_form.is_valid():
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 != password2:
                return HttpResponse("{'status': 'fail', 'msg':'pwd1 != pwd2'}", content_type='application/json')
            request.user.password = make_password(password1)
            request.user.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    """修改邮箱"""
    def post(self, request):
        email_form = UpdateEmailForm(request.POST)
        if email_form.is_valid():
            email = request.POST.get('email', '')
            request.user.email = email
            request.user.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        return HttpResponse("{'status': 'fail', 'msg':'fail'}", content_type='application/json')


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html')
    response.status_code = 500
    return response


def permission_denied(request):
    from django.shortcuts import render_to_response
    response = render_to_response('403.html')
    response.status_code = 403
    return response

