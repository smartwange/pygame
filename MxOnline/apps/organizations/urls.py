from django.conf.urls import url
from apps.organizations.views import orgList,askForm,orgDetail,orgTeacher,orgCourse,orgDesc


urlpatterns = [
    url(r'^list/$',orgList.as_view(),name='org_list'),
    url(r'^ask_form/$',askForm.as_view(),name='ask_form'),
    url(r'^(?P<org_id>\d+)/$',orgDetail.as_view(),name='org_detail'),
    url(r'^(?P<org_id>\d+)/teacher$',orgTeacher.as_view(),name='org_teacher'),
    url(r'^(?P<org_id>\d+)/course$',orgCourse.as_view(),name='org_course'),
    url(r'^(?P<org_id>\d+)/desc$',orgDesc.as_view(),name='org_desc')
]
