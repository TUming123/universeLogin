import time

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from lib.dosomething import dosomething
from .models import Message
from .models import MessageUser
from lib.myLog import myLog


log = myLog()
salt = "ming"


def formLogin(request):
    return render(request, "formSignIn.html")


def formSign(request):
    try:
        if request.method == 'POST':
            ID = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            if ID == "":
                log.try2sign(ID,log.getIp(request),"form")
                return render(request, "formSignUp.html", {
                    "msg": "请输入用户名"
                })
            if len(psw) < 6:
                log.try2sign(ID,log.getIp(request),"form")
                return render(request, "formSignUp.html", {
                    "msg": "请输入长度大于6的密码"
                })
            user1 = MessageUser.objects.filter(ID=ID)
            if not user1:
                messageuser = MessageUser(ID=ID, dpw=make_password(psw, salt))
                messageuser.save()
                log.succeed2sign(ID,log.getIp(request),"form")
                return HttpResponse("论坛用户注册成功")
            log.fail2sign(ID,log.getIp(request),"form")
            return render(request, "formSignUp.html", {
                "msg": "用户已存在"
            })
        return render(request, "formSignUp.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))

        return dosomething.doSomething()


def messageForm(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username", "")
            if username == "":
                log.fail2form(username,log.getIp(request))
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
            log.succeed2form(username,log.getIp(request))
            return HttpResponse("留言成功")
            # t1 = render(request, "messageForm.html", var_dict)
            # return render(request, "messageForm.html", var_dict)
        elif request.method == "GET":
            # logger.info('url:%s method:%s auth有用户登录'
            #             % (request.path, request.method))
            nameTag = 'username'
            username = ""
            try:
                # username = Signer(salt).unsign(request.GET[nameTag])
                username = request.session[nameTag]
                if not username or username == "":
                    log.fail2form(username,log.getIp(request))
                    return HttpResponse("未登录")
            except Exception as e:
                log.runtime(e,username,log.getIp(request))
                return HttpResponse("非法访问,错误提示" + e.__str__())
            return render(request, "messageForm.html", {
                'username': username,
            })
        return render(request, "messageForm.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))

        return dosomething.doSomething()


class FormLoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "formSignIn.html")

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            log.try2login(username,log.getIp(request),"form")
            if not username:
                log.fail2login(username,log.getIp(request),"form")
                return render(request, "formSignIn.html", {
                    "msg": "请输入用户名"
                })
            if not psw:
                log.fail2login(username,log.getIp(request),"form")
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
                log.succeed2login(username,log.getIp(request),"form")
                return HttpResponseRedirect(reverse("messageForm"))
                # 转到登陆完成页面
            else:
                log.fail2login(username,log.getIp(request),"form")
                return render(request, "formSignIn.html", {
                    "msg": "用户名或者密码不存在"
                })
                pass
        except Exception as e:
            log.runtime(e, "", log.getIp(request))

            return dosomething.doSomething()
