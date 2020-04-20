from django.contrib.auth.hashers import make_password
from django.core.signing import Signer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import time

from .models import Message
from .models import MessageUser
from django.views.generic.base import View
from django.contrib.auth import authenticate, login

salt = "ming"

def formLogin(request):
    return render(request, "formSignIn.html")

def formSign(request):
    if request.method == 'POST':
        ID = request.POST.get("username", "")
        psw = request.POST.get("psw", "")
        if ID == "":
            return render(request, "formSignUp.html", {
                "msg": "请输入用户名"
            })
        if len(psw) < 6:
            return render(request, "formSignUp.html", {
                "msg": "请输入长度大于6的密码"
            })
        user1 = MessageUser.objects.filter(ID=ID)
        if not user1:
            messageuser = MessageUser(ID=ID, dpw=make_password(psw, salt))
            messageuser.save()
            return HttpResponse("打赏用户注册成功")
        return render(request, "formSignUp.html", {
            "msg": "用户已存在"
        })
    return render(request, "formSignUp.html")

def messageForm(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        if username == "":
            return render(request, "formSignIn.html", {
                "msg": "请登录之后再评论"
            })
        message = Message()
        message.MID = username
        message.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        t = request.POST.get("name", "")
        message.name = t
        t = request.POST.get("address", "")
        message.address = t
        t = request.POST.get("email", "")
        message.email = t
        t = request.POST.get("message", "")
        message.message = t
        var_dict = {
            "message": message
        }
        message.save()
        return HttpResponse("留言成功")
        # t1 = render(request, "messageForm.html", var_dict)
        # return render(request, "messageForm.html", var_dict)
    elif request.method == "GET":
        nameTag = 'username'
        username = ""
        try:
            # username = Signer(salt).unsign(request.GET[nameTag])
            username = request.session[nameTag]
            if not username or username == "":
                return HttpResponse("未登录")
        except Exception as e:
            return HttpResponse(e.__str__())
        return render(request, "messageForm.html", {
            'username': username,
        })
    return render(request, "messageForm.html")


class FormLoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "formSignIn.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        psw = request.POST.get("psw", "")
        if not username:
            return render(request, "formSignIn.html", {
                "msg": "请输入用户名"
            })
        if not psw:
            return render(request, "formSignIn.html", {
                "msg": "请输入密码"
            })
        user1 = MessageUser.objects.filter(ID=username)
        # a = make_password(psw, salt)
        # a1 = make_password(psw, 'a')
        # a2 = make_password(psw, None)
        # a3 = make_password(psw, None)
        # a4 = make_password(psw, '')
        # b = user1.values('dpw')[0]['dpw']
        if user1 is not None and not len(user1) < 1 and make_password(psw, salt) == user1.values('dpw')[0]['dpw']:
            # r = reverse("messageForm")
            # nameTag = 'username'
            # r += "?" + nameTag + "=" + Signer(salt).sign(username)
            # return HttpResponseRedirect(r)
            request.session['username'] = username
            return HttpResponseRedirect(reverse("messageForm"))
            # 转到登陆完成页面
        else:
            return render(request, "formSignIn.html", {
                "msg": "用户名或者密码不存在"
            })
            pass

