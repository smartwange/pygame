import xadmin

from apps.courses.models import Course,Lesson,CourseResource,Video

# xadmin允许我们不继承任何东西


class GlobleSettings(object):
    site_title='在线学习网'
    site_footer='在线学习网'
    # 收起菜单栏
    menu_style='accordion'

class BaseSettings(object):
    enable_themes=True
    use_bootswatch=True

class CourseAdmin(object):
    list_display = ['name', 'desc','degree','learn_times','students','teacher']
    search_fields = ['name', 'desc','degree','students','teacher']
    list_filter = ['name', 'desc','degree','learn_times','students','teacher']
    list_editable = ['degree', 'desc']


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course', 'name']
    # course是课程的外键，过滤课程名 双下划线加name
    list_filter = ['course__name','name','add_time']

class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson','name','add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name','file', 'add_time']
    search_fields = ['course', 'name','file']
    list_filter = ['course', 'name','file', 'add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView,GlobleSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSettings)