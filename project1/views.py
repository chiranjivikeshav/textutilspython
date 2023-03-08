# this file is create by myself
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def analyse(request):
    djtext =request.POST.get('text','default')
    removepunc1 =request.POST.get('removepunc','off')
    touppercase1 =request.POST.get('Touppercase','off')
    countcharacter1 =request.POST.get('Countchar','off')


    analysed =""
    punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc1 =="on" and touppercase1=="on" and countcharacter1 =="on":
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        upperlettered=analysed.upper()
        numberofletter = len(analysed)
        params = {'perpose':'remove punctuation','analysed_text':analysed,'upper_lettter':upperlettered,'number_lettter':numberofletter}
        return render(request,'analyse.html',params)

    elif removepunc1 == "on":
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params = {'perpose':'remove punctuation','analysed_text':analysed}
        return render(request,'analyse.html',params)

    elif touppercase1=="on":
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        upperlettered=analysed.upper()
        params = {'upper_lettter':upperlettered}
        return render(request,'analyse.html',params)

    elif countcharacter1 =="on":
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        numberofletter=len(analysed)
        params = {'number_lettter':numberofletter}
        return render(request,'analyse.html',params)





# def capfirst(request):
#     return HttpResponse("keshav2")
# def spaceremove(request):
#     return HttpResponse("keshav2")
# def newlineremove(request):
#     return HttpResponse("keshav2")
# def charcount(request):
#     return HttpResponse("keshav2")