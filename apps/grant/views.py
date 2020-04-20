from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from apps.universe.models import UniverseUser
from lib.servGrant import servGrant

# Create your views here.

kgrant = "happytime"
kserv = "hamburger"
salt = "ming"


def grant(request):
    if request.method == "GET":
        client2grant = request.session['client2grant']
        if client2grant and len(client2grant) > 0:
            servgrant = servGrant(kgrant=kgrant, kserv=kserv)
            try:
                grant2client = servgrant.getClient(client2grant[0], client2grant[1])
                request.session['grant2client'] = grant2client
                return HttpResponseRedirect(reverse("universe"))
            except Exception as e:
                return HttpResponse(e.__str__())

    return render(request, "universe.html", {
        "msg": "认证服务器认证错误"
    })
