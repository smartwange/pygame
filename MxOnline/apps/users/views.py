from django.shortcuts import render
# 继承django内部中的view类
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.users.forms import LoginForm,CaptchaTestForm

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class LoginView(View):
    '''
    get方法,post方法是django内部中的view类的，直接重载
    get方法 处理get请求
    post方法  处理post请求
    request是django自动注入的
    '''

    def get(self,request, *args, **kwargs):
        # 判断是否登录 django2之前request.user.is_authenticated是一个方法，现在是一个属性
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        login_fom=CaptchaTestForm()
        return render(request,'login.html',{
            'login_fom':login_fom
        })

    def post(self,request, *args, **kwargs):
        # LoginForm既可以做表单验证，也可以做数据处理
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name= login_form.cleaned_data['username']
            password= login_form.cleaned_data['password']
        # user_name= request.POST.get('username','')
        # password= request.POST.get('password','')
#         字段验证 过于繁琐，直接配置django自带的form表单验证
#         if not user_name:
#             '''user_name是否为空'''
#             return render(request, 'login.html', {'msg': '请输入用户名'})
#         if not password:
#             return render(request, 'login.html', {'msg': '请输入密码'})



#         通过用户和密码查询用户是否存在，django内置方法authenticate(username,password),参数固定
#         验证成功之后得到一个userprofile对象，就是models中自定义的
#         返回none,代表用户密码错误
#         不建议通过模型验证，不利于代码维护,密码要加密处理
#         from apps.users.models import UserProfile
#         user=UserProfile.objects.get(username=user_name)
            user=authenticate(username=user_name,password=password)
            if user is not None:
                '''
                django 内置的login方法 登录用户 自动完成了cookie，保存session
                将django传递的过来的方法传递过去，将获取的user也传递过去
                '''
                login(request,user)
                # 使用render函数不会引起路由跳转
                # return render(request,'index.html')
                # 使用reverse到url的主页
                # request.user是通过settings.py文件的上下文设置的全局变量传递给模板的context_processors
                # 是否登录和cookie的sessionid有关
                return HttpResponseRedirect(reverse('index'))
            else:
                # 需要将表单数据显示回去
                return render(request,'login.html',{'msg':'用户名或密码错误','login_form':login_form})
        else:
            # debug模式下可以查看错误信息，将login_form对象返回给页面将错误渲染出来即可
            return render(request,'login.html',{'login_form':login_form})




