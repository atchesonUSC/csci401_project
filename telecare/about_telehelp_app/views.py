from django.shortcuts import render


def about(request, page):
    page = 'about_telehelp_' + page + '.html'
    args = {}
    return render(request, page, args)
