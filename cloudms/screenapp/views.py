from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudms.settings')
django.setup()
# Create your views here.
def screenproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, \
                                                msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "msg": linedata[2] \
                            , "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "MySingleWeb.html", {"data": datalist})

def homeproc(request):
    return  HttpResponse("<h1>这是首页具体功能请访问<a href='./index'>hero</a></h1>")