from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from apps.universe.models import UniverseUser
from lib.servApp import servApp
from apps.universe.models import UnionUser
from lib.myLog import myLog


log = myLog()

# Create your views here.

kserv = "hamburger"
salt = "ming"


def serv(request):
    try:
        if request.method == "GET":
            client2serv = request.session['client2serv']
            if client2serv and len(client2serv) > 0:
                servapp = servApp(kserv=kserv)
                try:
                    servapp.getClient(client2serv)
                    if servapp.qserv=="form":
                        formuser = UnionUser.objects.filter(UID=request.session['username'])
                        if formuser:
                            request.session['username'] = formuser[0].FID
                            return HttpResponseRedirect(reverse("messageForm"))
                        else:
                            log.runtime("universe",request.session['username'], log.getIp(request))
                            raise Exception("app serv 尚未注册或者关联用户")
                    elif servapp.qserv=="tips":
                        tipsuser = UnionUser.objects.filter(UID=request.session['username'])
                        if tipsuser:
                            request.session['username'] = tipsuser[0].TID
                            return HttpResponseRedirect(reverse("tips"))
                        else:
                            log.runtime("universe",request.session['username'], log.getIp(request))
                            raise Exception("app serv 尚未注册或者关联用户")
                    else:
                        log.runtime("universe",request.session['username'], log.getIp(request))
                        raise Exception("app serv 无此项服务")
                except Exception as e:
                    log.runtime(e, request.session['username'], log.getIp(request))
                    return HttpResponse(e.__str__())
        log.runtime("universe", request.session['username'], log.getIp(request))
        return render(request, "universe.html", {
            "msg": "认证服务器认证错误"
        })
    except Exception as e:
        log.runtime(e,"",log.getIp(request))
