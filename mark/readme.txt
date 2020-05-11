1、指定端口或ippython manage.py runserver 9999  Python manage.py runserver 192.168.10.145:9000
2、修改语言 LANGUAGE_CODE = 'zh-Hans'
3、创建新应用app，Tools --- Run manage.py Task... ---- 输入命令startapp blog
   并将创建的引用加入到根目录中，settings.py中INSTALLED_APPS 加入 'blog'
4、blog应用中的路由：blog文件夹中新建urls.py文件，新入相关请求包HttpRequest;
   引入视图文件，给视图文件定义路由；
   将blog下的urls文件，include到根目录下的urls.py文件中
5、views文件引用模板文件，并带参数
   params = {'names': '张三'}
   return render(request, 'hello.html',params)


