from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from apps.messageForm.models import MessageUser
from apps.tips.models import TipUser
from lib.client import client
from .models import UniverseUser, UnionUser
from lib.myLog import myLog
from lib.dosomething import dosomething


log = myLog()

salt = "ming"
cli = client("", "")


# Create your views here.

def createUnion(request):
    try:

        if request.method == 'POST':
            bindType = request.POST.get("createUnion", "")
            user1 = UniverseUser.objects.filter(ID=request.session["username"])
            if not user1 or bindType not in ["form", "tips"]:
                log.runtime("createUnion","",log.getIp(request))
                return HttpResponse("错误的用户绑定请求")
            username = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            if not username:
                log.fail2sign(username,log.getIp(request),"tip")
                return render(request, "createUnion.html", {
                    "msg": "请输入用户名"
                })
            if not psw:
                log.fail2sign(username,log.getIp(request),"tip")
                return render(request, "createUnion.html", {
                    "msg": "请输入密码"
                })
            user2 = MessageUser.objects.filter(ID=username)
            if bindType == "form":

                userTemp = UnionUser.objects.filter(FID=user2[0].ID)
                if not user2 or not user2[0]:
                    log.fail2sign(username,log.getIp(request),"tip")
                    return render(request, "createUnion.html", {
                        "msg": "目标用户名未注册"
                    })
                if userTemp:
                    log.fail2sign(username,log.getIp(request),"tip")
                    return render(request, "createUnion.html", {
                        "msg": "目标用户名已绑定其他用户,不可再绑定"
                    })
            else:
                userTemp = UnionUser.objects.filter(TID=user2[0].ID)
                if not user2 or not user2[0]:
                    log.fail2sign(username,log.getIp(request),"tip")
                    return render(request, "createUnion.html", {
                        "msg": "目标用户名未注册"
                    })
                if userTemp:
                    log.fail2sign(username,log.getIp(request),"tip")
                    return render(request, "createUnion.html", {
                        "msg": "目标用户名已绑定其他用户,不可再绑定"
                    })
            if user2 is not None and not len(user2) < 1 and make_password(psw, salt) == user2.values('dpw')[0]['dpw']:
                user1 = UnionUser.objects.filter(UID=request.session["username"])
                if not user1:
                    if bindType == "form":
                        user = UnionUser(UID=request.session["username"], FID=username, TID="")
                        log.succeed2sign(username,log.getIp(request),"tip")
                        user.save()
                    if bindType == "tips":
                        user = UnionUser(UID=request.session["username"], TID=username, FID="")
                        log.succeed2sign(username,log.getIp(request),"tip")
                        user.save()
                else:
                    if bindType == "form":
                        if user1[0].FID != "":
                            log.fail2sign(username,log.getIp(request),"tip")
                            return render(request, "createUnion.html", {
                                "msg": "本用户名已绑定其他用户,不可再绑定"
                            })
                        else:
                            log.succeed2sign(username,log.getIp(request),"tip")
                            user1[0].FID = username
                            user1[0].save()
                    if bindType == "tips":
                        if user1[0].TID != "":
                            log.fail2sign(username,log.getIp(request),"tip")
                            return render(request, "createUnion.html", {
                                "msg": "本用户名已绑定其他用户,不可再绑定"
                            })
                        else:
                            log.succeed2sign(username,log.getIp(request),"tip")
                            user1[0].TID = username
                            user1[0].save()
                return HttpResponse("绑定成功")
            else:
                log.fail2sign(username,log.getIp(request))
                return render(request, "createUnion.html", {
                    "msg": "用户名或者密码不存在"
                })

        if request.method == 'GET':
            if "username" in request.session and request.session["username"] != "":

                user1 = UniverseUser.objects.filter(ID=request.session["username"])
                if not user1:
                    return HttpResponse("错误的用户绑定请求")

                return render(request, "createUnion.html")

    except Exception as e:
        log.runtime(e, "", log.getIp(request))

        dosomething.doSomething()
        return dosomething.doSomething()


def universe(request):
    try:

        if request.method == 'POST':
            if 'auth2client' in request.session:
                del request.session['auth2client']
            if 'grant2client' in request.session:
                del request.session['grant2client']
            if 'Qgrant' in request.session:
                del request.session['Qgrant']
            nameTag = 'username'
            username = ""
            Qserv = request.POST.get("Qserv", "")
            if Qserv != "":
                request.session['Qserv'] = Qserv
            else:
                log.runtime("",username,log.getIp(request))
                return HttpResponse("未选择跳转登录页")
            try:
                # username = Signer(salt).unsign(request.GET[nameTag])
                username = request.session[nameTag]
                if not username or username == "" or cli.dpw == "":
                    log.runtime("",username,log.getIp(request))
                    return HttpResponse("未登录")
            except Exception as e:
                log.runtime(e,username,log.getIp(request))
                return HttpResponse(e.__str__())

            return HttpResponseRedirect(reverse("auth"))

        if request.method == 'GET':
            try:
                username = request.session['username']
                if 'grant2client' in request.session:
                    grant2client = request.session['grant2client']
                    cli.qserv = request.session['Qserv']
                    client2serv = cli.getGrant(grant2client)
                    request.session['client2serv'] = client2serv
                    return HttpResponseRedirect(reverse("serv"))
                elif 'Qgrant' in request.session:
                    cli.qgrant = request.session['Qgrant']
                    client2grant = cli.send2Grant()
                    request.session['client2grant'] = client2grant
                    return HttpResponseRedirect(reverse("grant"))
                elif 'auth2client' in request.session:
                    cli.dpw = make_password(cli.dpw, salt)
                    auth2client = request.session['auth2client']
                    cli.getAuth(auth2client)
                    request.session['Qgrant'] = "yes"
                    cli.qgrant = request.session['Qgrant']
                    client2grant = cli.send2Grant()
                    request.session['client2grant'] = client2grant
                    return HttpResponseRedirect(reverse("grant"))
                if username and cli.dpw != "":
                    return render(request, "universe.html", {
                        'username': username
                    })
                else:
                    log.runtime("",username,log.getIp(request))
                    return HttpResponse("未登录")
            finally:
                if 'grant2client' in request.session:
                    del request.session['grant2client']
                if 'Qgrant' in request.session:
                    del request.session['Qgrant']
                if 'auth2client' in request.session:
                    del request.session['auth2client']
    except Exception as e:
        log.runtime(e,"",log.getIp(request))

        return dosomething.doSomething()


def universeLogin(request):

    try:
        return render(request, "universeSignIn.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))


def universeSign(request):
    try:
        if request.method == 'POST':
            ID = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            if ID == "":
                log.try2sign(ID,log.getIp(request))
                return render(request, "universeSignUp.html", {
                    "msg": "请输入用户名"
                })
            if len(psw) < 6:
                log.try2sign(ID,log.getIp(request))
                return render(request, "universeSignUp.html", {
                    "msg": "请输入长度大于6的密码"
                })
            user1 = UniverseUser.objects.filter(ID=ID)
            if not user1:
                universeuser = UniverseUser(ID=ID, dpw=make_password(psw, salt))
                universeuser.save()
                log.succeed2sign(ID,log.getIp(request))
                return HttpResponse("统一用户注册成功")
            log.fail2sign(ID,log.getIp(request))
            return render(request, "universeSignUp.html", {
                "msg": "用户已存在"
            })
        return render(request, "universeSignUp.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))

        return dosomething.doSomething()


class universeLoginView(View):

    def get(self, request, *args, **kwargs):
        # log.system("","","try")
        return render(request, "universeSignIn.html")

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get("username", "")
            psw = request.POST.get("psw", "")
            log.try2login(username, log.getIp(request),"tip")
            if not username:
                log.fail2login(username,log.getIp(request),"tip")
                return render(request, "universeSignIn.html", {
                    "msg": "请输入用户名"
                })
            if not psw:
                log.fail2login(username,log.getIp(request),"tip")
                return render(request, "universeSignIn.html", {
                    "msg": "请输入密码"
                })
            user1 = UniverseUser.objects.filter(ID=username)
            # a = make_password(psw, salt)
            # a1 = make_password(psw, 'a')
            # a2 = make_password(psw, None)
            # a3 = make_password(psw, None)
            # a4 = make_password(psw, '')
            # b = user1.values('dpw')[0]['dpw']
            if user1 is not None and not len(user1) < 1 and make_password(psw, salt) == user1.values('dpw')[0]['dpw']:
                # r = reverse("universe")
                # nameTag = 'username'
                # r += "?" + nameTag + "=" + Signer(salt).sign(username)
                # return HttpResponseRedirect(r)
                request.session['username'] = username
                cli.dpw = psw
                log.succeed2login(username,log.getIp(request),"tip")
                return HttpResponseRedirect(reverse("universe"))
                # 转到登陆完成页面
            else:
                log.fail2login(username,log.getIp(request),"tip")
                return render(request, "universeSignIn.html", {
                    "msg": "用户名或者密码不存在"
                })
                pass
        except Exception as e:
            log.runtime(e, "", log.getIp(request))

            return dosomething.doSomething()
