from django.shortcuts import render


def waiting_room(request, page):
    page = 'waiting_room_' + page + '.html'
    args = {}
    return render(request, page, args)
