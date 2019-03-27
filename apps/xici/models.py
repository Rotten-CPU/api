from django.db import models
from datetime import datetime


class XiciModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='服务器地址')
    ip_address = models.CharField(max_length=200, verbose_name='IP地址')
    ip_type = models.CharField(max_length=200, verbose_name='IP类型')
    ip_speed = models.CharField(max_length=200, verbose_name='IP速度')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '免费代理IP'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
