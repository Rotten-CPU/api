# 项目


### 定时脚本采集
```
    1.爬取xici代理（存活时间>1天,速度<=1秒）
    2.验证代理可用性 请求百度,返回200即可
    3.入库 - 放api
```




### django 指令
```
django-admin startproject xxx
django-admin startapp xxx
mkdir apps extra_apps media static templates
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
### 配置xadmin2.0所需要的依赖
```
pip install -i https://pypi.douban.com/simple django django-reversion future django-crispy-forms django-formtools httplib2 six django-import-export
# 加速 -i https://pypi.douban.com/simple
settings.py 里添加如下
INSTALLED_APPS = [
    'xadmin',
    'crispy_forms',
]
urls.py 修改如下
import xadmin
from django.conf.urls import url, include
urlpatterns = [
    url('xadmin/', xadmin.site.urls),
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONG = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = False
```
