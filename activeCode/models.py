from django.db import models
from project.models import ProjectModel


class ActiveCodeModel(models.Model):

    code = models.CharField('激活码', max_length=500)
    project = models.ForeignKey(ProjectModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='项目')
    is_active = models.BooleanField('是否激活', default=False)
    is_disable = models.BooleanField('是否禁用', default=False)
    active_time = models.DateTimeField('激活时间', null=True, blank=True)
    invalid_time = models.DateTimeField('失效时间', null=True, blank=True)
    note = models.CharField('备注', max_length=500, null=True, blank=True)
    add_time = models.DateTimeField('添加时间', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = '激活码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.code}"
