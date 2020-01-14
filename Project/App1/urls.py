"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$', views.test),   # method view,  must end with 'test'
    url(r'^test/$', views.test),  # method view,  must end with 'test/'

    url(r'^myclassview/$', views.MyClassView.as_view() ),    # class view
    url(r'^time/(\d+)/(\d+)$', views.get_time),        # Regular Expressions in ()    # param1 param2 不命名则是位置参数
    url(r'^time/(?P<year>\d{4})/(?P<month>\d{2})/$', views.get_date),  # year month  命名参数 更好
]


# url 支持 【正则表达式】写法 => 在view中获取 url参数 就是采用正则表达式写法的，
'''
Regular Expressions :
Symbol   |    Matches
. (dot)  |    Any single character
\d       |    Any single digit
[A-Z]    |    Any character between A and Z (uppercase)
[a-z]    |    Any character between a and z (lowercase)
[A-Za-z] |    Any character between a and z (case-insensitive)
+        |    One or more of the previous expression (e.g., \d+ matches one or more digits)
[^/]+    |    One or more characters until (and not including) a forward slash
?        |    Zero or one of the previous expression (e.g., \d? matches zero or one digits)
*        |    Zero or more of the previous expression (e.g., \d* matches zero, one or more than one digit)
{1,3}    |    Between one and three (inclusive) of the previous expression (e.g., \d{1,3} matches one, two or three digits)
'''
'''
. (dot)	  任意单一字符
\d	      任意一位数字
[A-Z]	  A 到 Z中任意一个字符（大写）
[a-z]	  a 到 z中任意一个字符（小写）
[A-Za-z]  a 到 z中任意一个字符（不区分大小写）
+	      匹配一个或更多 (例如, \d+ 匹配一个或 多个数字字符)
[^/]+	  一个或多个不为‘/’的字符
*	      零个或一个之前的表达式（例如：\d? 匹配零个或一个数字）
*	      匹配0个或更多 (例如, \d* 匹配0个 或更多数字字符)
{1,3}	  介于一个和三个（包含）之前的表达式（例如，\d{1,3}匹配一个或两个或三个数字）
'''
