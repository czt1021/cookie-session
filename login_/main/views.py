from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

user_info = {
    'derek':{'pwd':'123123'},
    'jack':{'pwd':'456456'}
}

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)         #获取key的value
        if not dic:
            return render(request,'login.html')
        if dic['pwd'] == p:
            result = redirect('/index/')
            result.set_cookie('username',u)    #设置cookie值
            #result.set_cookie('username', u, max_age=10)  # 设置cookie失效时间10s
            return result
        else:
            return render(request,'login.html')

def index(request):
    v = request.COOKIES.get('username')
    if not v:
        return redirect('/login/')
    return render(request,'index.html',{'current_user':v})