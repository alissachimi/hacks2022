from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    return render(request, 'home.html')

def miles(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("miles", ""):
            response1 = request.POST.get("miles", "")
            return render(request, 'page2.html')
        else:
            message = "Error: Please enter a valid mile amount"
    
    return render(request, 'miles.html')

def page2(request):
    message =""
    response2 = request.POST.get("vmodel", "")
    if request.method == "POST":
        if response2 == "2000":
            return redirect('a2000.html')
        elif response2 == "2001":
            return redirect('a2001.html')
        elif response2 == "2002":
            return redirect('a2002.html')
        elif response2 == "2003":
            return redirect('a2003.html')
        elif response2 == "2004":
            return redirect('a2004.html')
        elif response2 == "2005":
            return redirect('a2005.html')
        elif response2 == "2006":
            return redirect('a2006.html')
        elif response2 == "2007":
            return redirect('a2007.html')
        elif response2 == "2008":
            return redirect('a2008.html')
        elif response2 == "2009":
            return redirect('a2009.html')
        elif response2 == "2010":
            return redirect('a2010.html')
        elif response2 == "2011":
            return redirect('a2011.html')
        elif response2 == "2012":
            return redirect('a2012.html')
        elif response2 == "2013":
            return redirect('a2013.html')
        elif response2 == "2014":
            return redirect('a2014.html')
        elif response2 == "2015":
            return redirect('a2015.html')
        else:
            message = "Error: Please enter a supported year (i.e. 2000-2015)"
    context = {"message": message}
    return render(request, 'page2.html', context)

def mult(a,b):
    return a * b

def a2000(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 341.01999)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2000.html", context)

def a2001(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 348.10111)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2001.html", context)

def a2002(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 344.72148)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2002.html", context)

def a2003(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 340.21532)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2003.html", context)

def a2004(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 313.01741)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2004.html", context)

def a2005(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 313.01741)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2005.html", context)

def a2006(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 319.29385)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2006.html", context)

def a2007(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 319.29385)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2007.html", context)

def a2008(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 319.29385)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2008.html", context)

def a2009(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 319.29385)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2009.html", context)

def a2010(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 276.32436)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2010.html", context)

def a2011(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 273.588)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2011.html", context)

def a2012(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 264.89802)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2012.html", context)

def a2013(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 263.77148)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2013.html", context)

def a2014(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 264.89802)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2014.html", context)

def a2015(request):
    message = 0
    intt = request.POST.get("miles","")
    if request.method == "POST":
        if request.POST.get("miles",""):
            message = mult(int(intt), 265.86363)
        else:
            message = 0
    context = {"message": message}
    return render(request, "a2015.html", context)

def yay(request):
    return render(request, 'yay.html')
