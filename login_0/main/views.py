from  django.shortcuts import render,HttpResponse,redirect

def login(request):
    if request.method == 'GET':
        return render(request ,'login.html')
    elif request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == "123":
            # 往session字典内写入用户状态和数据
            request.session['username'] = user
            request.session['if_login'] = True  # 可不加 直接判断username也可以
            if request.POST.get('session') == '1':  # 单独设置超时时间，当前session生效，不影响全局
                request.session.set_expiry(10)  # 10秒
            return redirect('/index/')
        else:
            return redirect('/login/')

def index(request):
    # 获取当前用户的随机字符串
    # 根据随机字符串获取对应信息
    # 不允许重复登录
    if request.session.get('if_login'):
        return render(request, 'index.html')
    else:
        return redirect('/login/')