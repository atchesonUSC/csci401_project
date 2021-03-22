from django.shortcuts import render


# About USC TeleHELP
def about_telehelp(request):
    page = 'about_telehelp.html'
    args = {}
    return render(request, page, args)


def install(request):
    page = 'install.html'
    args = {}
    return render(request, page, args)


def cam_mic(request):
    page = 'cam_mic.html'
    args = {}
    return render(request, page, args)


def internet(request):
    page = 'internet.html'
    args = {}
    return render(request, page, args)


def help_center(request):
    page = 'help.html'
    args = {}
    return render(request, page, args)



