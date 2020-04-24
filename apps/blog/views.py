from django.shortcuts import render
from lib.myLog import myLog


log = myLog()

# Create your views here.

def blog(request):
    try:
        log.blog("webuser",log.getIp(request))
        return render(request, "blog.html")
    except Exception as e:
        log.runtime(e,"",log.getIp(request))
