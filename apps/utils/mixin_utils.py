from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from acticle.models import Article
from operation.models import Message

# 热门推荐:阅读人数
def get_fav_articles():
    return Article.objects.all().order_by('-see_num')[:5]


# 获取当前日期
def get_date():
    return datetime.now().strftime('%Y-%m-%d')


# 获取当前星期数
def get_weekday():
    week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday = datetime.now().weekday()
    return week_list[weekday]


# 获取最新留言
def get_new_message():
    return Message.objects.all().order_by('-add_time')[:5]


# login
class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
