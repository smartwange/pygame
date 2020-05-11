from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# 基类
class BaseModel(models.Model):
    # 不能直接datetime.now(),这样会在一引用的时候生成时间，而我们需要在课程添加或者其他操作的时候生成时间
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        # abstract=True调用时阻止将这个class生成一张表
        abstract=True

# 改写原有的用户管理表，继承已有的字段重新生成新加的表
GENDER_CHOICES=(
    ('male','男'),
    ('female','女')
)

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=100,verbose_name='昵称',default='')
    birthday=models.DateField(verbose_name='生日',null=True,blank=True)
    gender=models.CharField(max_length=6,verbose_name='性别',choices=GENDER_CHOICES)
    address = models.CharField(max_length=100,verbose_name='地址',default='')
    # 将unique=True去掉，在用户注册中解决
    mobile=models.CharField(max_length=11,verbose_name='手机号码')
    # 或者FileField ,upload_to后面相对于media的路径 media/head_img/年/月
    image = models.ImageField(verbose_name='头像',upload_to='head_img/%Y%m',default='default.jpg')

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        if self.nick_name:
            return  self.nick_name
        else:
            return self.username