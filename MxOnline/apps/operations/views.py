from django.shortcuts import render
from django.views.generic.base import View
from apps.operations.forms import addFavForm
from django.http import JsonResponse
from apps.operations.models import UserFavorite
from apps.organizations.models import CourseOrg,Teacher
from apps.courses.models import Course

class addFavView(View):
    def post(self, request, *args, **kwargs):
        '''先判断是否登录'''
        if not request.user.is_authenticated:
            return JsonResponse({
                'status': 'fail',
                'msg': '用户未登录'
            })

        add_fav_form=addFavForm(request.POST)
        if add_fav_form.is_valid():
            fav_id=request.POST.get('fav_id',0)
            fav_type=request.POST.get('fav_type',0)
            user=request.user
            #是否已收藏,收藏过就要将收藏记录删掉，收藏次数减一
            exist_fav=UserFavorite.objects.filter(user=user,fav_id=fav_id,fav_type=fav_type)
            if exist_fav:
               exist_fav.delete()
               if fav_type==1:
                   course=Course.objects.get(id=fav_id)
                   course.fav_nums-=1
                   course.save()
               elif fav_type==2:
                   course_org=CourseOrg.objects.get(id=fav_id)
                   course_org.fav_nums-=1
                   course_org.save()
               elif fav_type==3:
                   teacher=Teacher.objects.get(id=fav_id)
                   teacher.fav_nums-=1
                   teacher.save()

               return JsonResponse({
                   'status': 'success',
                   'msg': '收藏'
               })
            else:
                user_fav=UserFavorite()
                user_fav.user=user
                user_fav.fav_id=fav_id
                user_fav.fav_type=fav_type
                user_fav.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '已收藏'
                })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '参数错误111111'
            })
