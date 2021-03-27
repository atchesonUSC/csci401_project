from django.shortcuts import render


def about(request, page):
    page = 'module_base.html'
    #page = 'about_telehelp_' + page + '.html'
    args = {}
    return render(request, page, args)
