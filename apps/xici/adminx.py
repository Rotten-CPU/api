import xadmin
from xadmin import views


class BaseSetting(object):
    site_title = '后台管理系统'
    site_footer = '后台管理系统'

    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, BaseSetting)

from .models import XiciModel


class XiciX(object):
    list_display = ["name", "ip_address", "ip_type", "ip_speed", "update_time", "add_time"]
    ordering = ["-id"]


xadmin.site.register(XiciModel, XiciX)

