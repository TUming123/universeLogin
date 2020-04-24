from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from apps.universe.models import UniverseUser
from lib.servGrant import servGrant
from lib.myLog import myLog


log = myLog()

# Create your views here.

kgrant = "happytime"
kserv = "hamburger"
salt = "ming"


def grant(request):
    try:
        if request.method == "GET":
            client2grant = request.session['client2grant']
            if client2grant and len(client2grant) > 0:
                servgrant = servGrant(kgrant=kgrant, kserv=kserv)
                try:
                    grant2client = servgrant.getClient(client2grant[0], client2grant[1])
                    request.session['grant2client'] = grant2client
                    return HttpResponseRedirect(reverse("universe"))
                except Exception as e:
                    log.runtime(e,request.session['username'],log.getIp(request))
                    return HttpResponse(e.__str__())
        log.runtime("", "", log.getIp(request))
        return render(request, "universe.html", {
            "msg": "认证服务器认证错误"
        })
    except Exception as e:
        log.runtime(e,"",log.getIp(request))
