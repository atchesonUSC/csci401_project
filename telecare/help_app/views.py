from django.shortcuts import render


def help_center(request):
    page = 'help.html'
    args = {}
    return render(request, page, args)
