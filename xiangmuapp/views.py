from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'register.html')

def reg(request):  #注册页面
    if request.method=='GET':
        return render(request,'register.html')
    else:#post提交
        #获取注册信息
        username=request.POST.get('user_name')
        password=request.POST.get('pwd')
        email = request.POST.get ('email')
        allow = request.POST.get ('allow')
        if not all([username,password,email]):
            return render(request,'register.html',{'mig':'数据不完整'})
