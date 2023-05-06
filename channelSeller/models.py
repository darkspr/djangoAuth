from django.db import models
from django.contrib.auth.models import User


class ChannelModel(models.Model):
    account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='代理')
    is_active = models.BooleanField('权限', default=True)
    note = models.CharField('备注', max_length=500, null=True, blank=True)
    add_time = models.DateTimeField('上传时间', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = '代理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.account.username}"
