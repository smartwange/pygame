from django.shortcuts import render
# 取数据，将模型里定义的函数引入调用即可
from apps.message_form.models import Message


# 接受一个django传进来的参数request对象，每个请求包装成的对象
def message_form(request):
    # Message类中注入了一个objects对象，他是所有操作的核心
    # 它可以取数据，all()方法取出所有、


    # 在return前打断点，使用dubug模式查看获取的对象 QuerySet
    # QuerySet对象是python中内置的一个类型，可以对他进行for循环
    # 对QuerySet进行切片操作，可以QuerySet对象当作一个list列表
    # all_message = Message.objects.all()[:1]
    # QuerySet只是执行了一条sql语句，本身没有执行sql操作
    # all_message=Message.objects.all()
    # sliced_message=Message.objects.all()[:1]
    # # SELECT `message`.`name`, `message`.`email`, `message`.`address`, `message`.`message` FROM `message`  LIMIT 1
    # print(sliced_message.query)
    # # SELECT `message`.`name`, `message`.`email`, `message`.`address`, `message`.`message` FROM `message`
    # print(all_message.query)
    # # 打印时才执行了sql操作
    # print(sliced_message.name)
    # --------------------------------------------------------
    # 2 . filter操作，相当于where语句
    # all_message = Message.objects.filter(name='wzy')
    # # SELECT `message`.`name`, `message`.`email`, `message`.`address`, `message`.`message` FROM `message` WHERE `message`.`name` = wzy
    # print(all_message.query)
    # # for循环里才执行了sql操作
    # for message in all_message:
    #     # message是all_message 的实例  Message object (bobby)
    #     print(message.name)
    # --------------------------------------------------------
    # 3. get方法，返回的是一个对象 而不是queryset
    # 只返回一条数据，要求比较严格，如果数据不存在或者有多条会抛出异常
    # 和返回QuerySet对象不同，get方法一执行就开始执行sql语句
    # try:
    #     message = Message.objects.get(name='wzy')
    #     print(message.email)
    # #     偷懒写法，所有的异常
    # # except Exception as e:
    # # 常规写法，具体到那种异常
    # except Message.DoesNotExist as e:
    #     pass
    # except Message.MultipleObjectsReturned as e:
    #     pass
    # 删除数据
    # 删除所有
    # message =Message.objects.all()
    # 使用get或filter删除一个
    # message = Message.objects.filter(name='wzy')
    # message.delete()
    # 新增数据 先实例化一个messages对象
    # messages = Message()
    # messages.name='ewe'
    # messages.email='ewe@qq.com'
    # messages.address='ewwe'
    # messages.message='rrrrrrr'
    # # save()方法  如果数据存在则 修改，如果不存在则 新增
    # messages.save()

    # 从前端页面接受数据，通过debug模式，返回前端一个<WSGIRequest: POST '/message_form/'> 即WSGIRequest对象
    # 表单提交后，通过request.POST获取一个dict字典，通过get()方法获取val值
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message_text = request.POST.get('message', '')
        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()
        return render(request, 'message_form.html',{
                'message': message
            })
    if request.method=='GET':
        var_dict = {}
        all_message = Message.objects.all()
        if all_message:
            message = all_message[0]
            var_dict={
                'message': message
            }
        return render(request, 'message_form.html',var_dict)
