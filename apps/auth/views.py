from django.shortcuts import render
from lib.message import message
from lib.servAuth import servAuth
from apps.universe.models import UniverseUser
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.signing import Signer
# Create your views here.

kgrant = "happytime"
salt = "ming"

def auth(request):
    if request.method=="GET":
        username = request.session['username']
        if username and len(username)>0:
            servauth = servAuth(kgrant=kgrant)
            user1 = UniverseUser.objects.filter(ID=username)
            if user1 and user1[0]:
                servauth.generateTgant()
                servauth.dpw = user1[0].dpw
                auth2client = servauth.send2Client()
                request.session['auth2client'] = auth2client
                return HttpResponseRedirect(reverse("universe"))
            else:
                return HttpResponse("auth server 认证失败")


    return render(request, "universe.html",{
        "msg": "认证服务器认证错误"
    })