from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher
from apps.organizations.models import CourseOrg

# 1、设计表结构重点：
'''
   实体1 <关系> 实体2
   课程  章节  视频   课程资源
'''
# 2、实体的具体字段
# 3、每个字段的类型，是否必填
# tag课程标签用来做课程推荐用，有相同课程标签的课程
# detail课程详情，富文本
class Course(BaseModel):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='讲师')
    course_org=models.ForeignKey(CourseOrg,blank=True,null=True,on_delete=models.CASCADE,verbose_name='机构')
    name=models.CharField(max_length=50,verbose_name='课程名')
    desc = models.CharField(max_length=300,verbose_name='课程描述')
    learn_times=models.IntegerField(default=0,verbose_name='学习时长(分钟数)')
    degree=models.CharField(max_length=2,verbose_name='难度',choices=(('cj','初级'),('zj','中级'),('gj','高级')))
    students=models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums=models.IntegerField(default=0,verbose_name='收藏人数')
    click_nums=models.IntegerField(default=0,verbose_name='点击数')
    catagory = models.CharField(verbose_name='课程类别',default=u"后端开发",max_length=20)
    tag=models.CharField(default='',verbose_name='课程标签',max_length=10)
    youneed_know=models.CharField(default='',verbose_name='课程须知',max_length=300)
    teacher_tell = models.CharField(default='',max_length=300,verbose_name='老师告诉你')

    detail=models.TextField(verbose_name='课程详情')
    image=models.ImageField(upload_to='course/%Y/%m',verbose_name='封面图',max_length=100)
    is_classics=models.BooleanField(default=False,verbose_name='是否经典')

    class Meta:
        verbose_name='课程信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        # return必须为必填项
        return self.name

class Lesson(BaseModel):
    # on_delete表示删除当前外键后，当前的数据怎么办
    # CASCADE表示当前课程被删，对应的章节也删除
    # SET_NULL 当前课程被删，对应的章节置为null,并且加上,null=True,blank=True否则冲突报错
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    name = models.CharField(max_length=100,verbose_name='章节名')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')


    class Meta:
        verbose_name='课程章节'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.course.name+'('+self.name+')'


class Video(BaseModel):
    lesson=models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='视频名')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    url=models.CharField(max_length=200,verbose_name=u'访问地址')


    class Meta:
        verbose_name='视频'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    name = models.CharField(max_length=100,verbose_name=u'名称')
    file=models.FileField(upload_to='course/resource/%Y/%m',verbose_name='下载地址',max_length=200)

    class Meta:
        verbose_name='课程资源'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name