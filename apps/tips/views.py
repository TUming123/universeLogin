import time

from django.contrib.auth.hashers import make_password
from django.core.signing import Signer
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from lib.dosomething import dosomething
from .models import TipMessage
from .models import TipUser
from lib.myLog import myLog


log = myLog()

salt = "ming"


# Create your views here.

def tips(request):
    try:
        if request.method == 'POST':
            amount = request.POST.get("amount", "0")
            username = request.POST.get("username", "")
            if username == "":
                log.fail2tip(username,log.getIp(request))
                return render(request, "tipsSignIn.html", {
                    "msg": "请登录之后再打赏"
                })
            if amount.isnumeric():
                amount = int(amount)
                tipmessage = TipMessage(TID=username, amount=amount,
                                        date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                tipmessage.save()
                log.succeed2tip(username,log.getIp(request))
                return HttpResponse("打赏成功")
            log.fail2tip(username,log.getIp(request))
            return render(request, "tips.html", {
                'username': username,
            })
        if request.method == 'GET':
            nameTag = 'username'
            username = ""
            try:
                username = request.session[nameTag]
                if not username or username== "":
                    return HttpResponse("未登录")
            #     username = Signer(salt).unsign(request.session[nameTag])
            except Exception as e:
                log.runtime(e,username,log.getIp(request))
                return HttpResponse(e.__str__())
            return render(request, "tips.html", {
                'username': username,
            })
        return render(request, "tips.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))

        return dosomething.doSomething()


def tipsLogin(request):
    log.try2login("",log.getIp(request),"tip")
    return render(request, "tipsSignIn.html")


def tipsSign(request):
    try:
        if request.method == 'POST':
            ID = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            if ID == "":
                log.fail2sign(ID,log.getIp(request),"tip")
                return render(request, "tipsSignUp.html", {
                    "msg": "请输入用户名"
                })
            if len(psw) < 6:
                log.fail2sign(ID,log.getIp(request),"tip")
                return render(request, "tipsSignUp.html", {
                    "msg": "请输入长度大于6的密码"
                })
            user1 = TipUser.objects.filter(ID=ID)
            if not user1:
                tipsuser = TipUser(ID=ID, dpw=make_password(psw, salt))
                tipsuser.save()
                log.succeed2sign(ID,log.getIp(request),"tip")
                return HttpResponse("打赏用户注册成功")
            log.fail2sign(ID,log.getIp(request),"tip")
            return render(request, "tipsSignUp.html", {
                "msg": "用户已存在"
            })
        log.try2sign("",log.getIp(request),"tip")
        return render(request, "tipsSignUp.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))

        return dosomething.doSomething()


class TipsLoginView(View):

    def get(self, request, *args, **kwargs):
        log.try2login("",log.getIp(request),"tip")
        return render(request, "tipsSignIn.html")

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            if not username:
                log.fail2sign(username,log.getIp(request),"tip")
                return render(request, "tipsSignIn.html", {
                    "msg": "请输入用户名"
                })
            if not psw:
                log.fail2sign(username,log.getIp(request),"tip")
                return render(request, "tipsSignIn.html", {
                    "msg": "请输入密码"
                })
            user1 = TipUser.objects.filter(ID=username)
            # a = make_password(psw, salt)
            # a1 = make_password(psw, 'a')
            # a2 = make_password(psw, None)
            # a3 = make_password(psw, None)
            # a4 = make_password(psw, '')
            # b = user1.values('dpw')[0]['dpw']
            if user1 is not None and not len(user1) < 1 and make_password(psw, salt) == user1.values('dpw')[0]['dpw']:
                # r = reverse("tips")
                # nameTag = 'username'
                # r += "?" + nameTag + "=" + Signer(salt).sign(username)
                # request.session['username'] = username
                # return HttpResponseRedirect(r)
                log.succeed2sign(username,log.getIp(request),"tip")
                request.session['username'] = username
                return HttpResponseRedirect(reverse("tips"))
                # 转到登陆完成页面
            else:
                log.fail2sign(username,log.getIp(request),"tip")
                return render(request, "tipsSignIn.html", {
                    "msg": "用户名或者密码不存在"
                })
        except Exception as e:
            log.runtime(e, "", log.getIp(request))

            return dosomething.doSomething()

    # def get(self, request, *args, **kwargs):
    #     return render(request, "tipsSignIn.html")
    #
    # def post(self, request, *args, **kwargs):
    #     username = request.POST.get("username", "")
    #     psw = request.POST.get("psw", "")
    #     if not username:
    #         return render(request, "tipsSignIn.html", {
    #             "msg":"请输入用户名"
    #         })
    #     if not psw:
    #         return render(request, "tipsSignIn.html", {
    #             "msg":"请输入密码"
    #         })
    #     try:
    #         user = authenticate(username=username, password=psw)
    #         if user is not None:
    #             login(request, user)
    #             return HttpResponseRedirect(reverse("tips"))
    #             # 转到登陆完成页面
    #         else:
    #             return render(request, "tipsSignIn.html", {
    #                 "msg":"用户名或者密码不存在"
    #             })
    #             pass
    #     except Exception as e:
    #         pass
