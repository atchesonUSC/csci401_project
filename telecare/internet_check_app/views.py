from django.shortcuts import render


# Create your views here.
def internet(request, page):
    page = 'internet_check_' + page + '.html'
    args = {}
    return render(request, page, args)
