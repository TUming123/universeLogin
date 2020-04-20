from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from lib.client import client
from .models import UniverseUser

salt = "ming"
cli = client("", "")


# Create your views here.

def universe(request):
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
            return HttpResponse("未选择跳转登录页")
        try:
            # username = Signer(salt).unsign(request.GET[nameTag])
            username = request.session[nameTag]
            if not username or username == "" or cli.dpw == "":
                return HttpResponse("未登录")
        except Exception as e:
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
                return HttpResponse("未登录")
        finally:
            if 'grant2client' in request.session:
                del request.session['grant2client']
            if 'Qgrant' in request.session:
                del request.session['Qgrant']
            if 'auth2client' in request.session:
                del request.session['auth2client']


def universeLogin(request):
    return render(request, "universeSignIn.html")


def universeSign(request):
    if request.method == 'POST':
        ID = request.POST.get("username", "")
        psw = request.POST.get("psw", "")
        if ID == "":
            return render(request, "universeSignUp.html", {
                "msg": "请输入用户名"
            })
        if len(psw) < 6:
            return render(request, "universeSignUp.html", {
                "msg": "请输入长度大于6的密码"
            })
        user1 = UniverseUser.objects.filter(ID=ID)
        if not user1:
            universeuser = UniverseUser(ID=ID, dpw=make_password(psw, salt))
            universeuser.save()
            return HttpResponse("统一用户注册成功")
        return render(request, "universeSignUp.html", {
            "msg": "用户已存在"
        })
    return render(request, "universeSignUp.html")


class universeLoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "universeSignIn.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        psw = request.POST.get("psw", "")
        if not username:
            return render(request, "universeSignIn.html", {
                "msg": "请输入用户名"
            })
        if not psw:
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
            return HttpResponseRedirect(reverse("universe"))
            # 转到登陆完成页面
        else:
            return render(request, "universeSignIn.html", {
                "msg": "用户名或者密码不存在"
            })
            pass
