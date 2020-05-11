from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.models import CourseOrg,City
from apps.organizations.forms import addAskForm
from django.http import JsonResponse
# Create your views here.
class orgList(View):
    def get(self,request, *args, **kwargs):
        org_all=CourseOrg.objects.all()
        all_city=City.objects.all()
        hot_org=org_all.order_by('-click_nums')[:3]
        # 获取培训机构类别
        cate=request.GET.get('ct','')
        if cate:
            org_all=org_all.filter(category=cate)

        # 获取城市
        city_id=request.GET.get('city','')
        if city_id:
            if city_id.isdigit():
                org_all = org_all.filter(city_id=city_id)

        # 排序 order_by负的表示倒序，
        sort=request.GET.get('sort','')
        if sort == 'students':
            org_all=org_all.order_by('-students')
        elif sort == 'courses':
            org_all=org_all.order_by('-course_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        org_nums = org_all.count()
         # 分页  per_page每页显示5条数据
        p = Paginator(org_all,per_page=5, request=request)
        org = p.page(page)
        return render(request,'org-list.html',{
            'org_all':org,
            'org_nums':org_nums,
            'all_city':all_city,
            'category':cate,
            'city_id':city_id,
            'sort':sort,
            'hot_org':hot_org
        })


class askForm(View):
    def post(self,request, *args, **kwargs):
        # 实例化 addAskForm  ,判断这个model form是否有问题
        # commit=True立即保存  返回usr_ask实例，并返回给前端页面
        ask_form=addAskForm(request.POST)
        if ask_form.is_valid():
            ask_form.save(commit=True)
            return JsonResponse({
                'status':'success'
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg':'提交出错'
            })


class orgDetail(View):
    def get(self,request,org_id, *args, **kwargs):
        nav_name = 'detail'
        '''根据org_id查询对应的机构和课程'''
        org_info=CourseOrg.objects.filter(id=int(org_id))[0]
        org_info.click_nums+=1
        org_info.save()

        all_courses=org_info.course_set.all()[:3]
        all_teachers = org_info.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html',{
            'org_info':org_info,
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'nav_name':nav_name
        })

class orgTeacher(View):
    def get(self, request, org_id, *args, **kwargs):
        nav_name='teacher'
        '''根据org_id查询对应的机构和课程'''
        org_info = CourseOrg.objects.filter(id=int(org_id))[0]
        org_info.click_nums += 1
        org_info.save()

        all_teachers = org_info.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'org_info': org_info,
            'all_teachers': all_teachers,
            'nav_name': nav_name
        })

class orgCourse(View):
    def get(self, request, org_id, *args, **kwargs):
        nav_name = 'course'
        '''根据org_id查询对应的机构和课程'''
        org_info = CourseOrg.objects.filter(id=int(org_id))[0]
        org_info.click_nums += 1
        org_info.save()

        all_courses = org_info.course_set.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

         # 分页  per_page每页显示5条数据
        p = Paginator(all_courses,per_page=2, request=request)
        courses = p.page(page)

        return render(request, 'org-detail-course.html', {
            'org_info': org_info,
            'all_courses': courses,
            'nav_name': nav_name
        })

class orgDesc(View):
    def get(self, request, org_id, *args, **kwargs):
        nav_name = 'desc'

        '''根据org_id查询对应的机构和课程'''
        org_info = CourseOrg.objects.filter(id=int(org_id))[0]
        org_info.click_nums += 1
        org_info.save()

        return render(request, 'org-detail-desc.html', {
            'org_info': org_info,
            'nav_name': nav_name
        })