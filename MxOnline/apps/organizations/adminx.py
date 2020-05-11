import xadmin

from apps.organizations.models import Teacher,CourseOrg,City

# xadmin允许我们不继承任何东西
class TeacherAdmin(object):
    list_display = ['org','name', 'work_years', 'work_company']
    search_fields = ['org','name','work_years', 'work_company']
    list_filter = ['org','name', 'work_years', 'work_company']

class CourseOrgAdmin(object):
    list_display = [ 'name', 'desc','fav_nums','click_nums']
    search_fields = ['name', 'desc','fav_nums','click_nums']
    list_filter = ['name', 'desc', 'fav_nums','click_nums']


class CityAdmin(object):
    '''
    xadmin的管理器中有三个配置项
    第一个时列表项，可模型中定义的字段一样
    第二个搜索范围....
    第三个过滤范围....
    第三个可以修改范围....
    '''
    list_display=['id','name','desc']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']
    list_editable=['name','desc']

xadmin.site.register(Teacher,TeacherAdmin)

xadmin.site.register(CourseOrg,CourseOrgAdmin)

xadmin.site.register(City,CityAdmin)