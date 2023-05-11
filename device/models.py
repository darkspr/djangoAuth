from django.db import models


class DeviceModel(models.Model):
    device_id = models.CharField('设备ID', max_length=500)
    note = models.CharField('备注', max_length=500, null=True, blank=True)
    add_time = models.DateTimeField('上传时间', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.device_id}"
