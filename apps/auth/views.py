from django.shortcuts import render

from lib.dosomething import dosomething
from lib.message import message
from lib.servAuth import servAuth
from apps.universe.models import UniverseUser
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.signing import Signer
import logging
# Create your views here.
# import logging
from lib.myLog import myLog


log = myLog()


# logger = logging.getLogger('auth')
kgrant = "happytime"
salt = "ming"

def auth(request):
    try:
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
                    # logger.info('username:%s url:%s method:%s auth服务器接受client信息并返回' %
                    #             (username, request.path, request.method))
                    return HttpResponseRedirect(reverse("universe"))
                else:
                    # logger.info('url:%s method:%s auth服务器接受client信息并返回' % (request.path, request.method))
                    log.runtime("",username, log.getIp(request))
                    return HttpResponse("auth server 认证失败")

        log.runtime("","", log.getIp(request))
        return render(request, "universe.html",{
            "msg": "认证服务器认证错误"
        })
    except Exception as e:
        log.runtime(e,"",log.getIp(request))
        return dosomething.doSomething()