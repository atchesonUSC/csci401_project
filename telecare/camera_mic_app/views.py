from django.shortcuts import render


def cam_mic_user_status(request):
    page = 'Cam_Mic_0.html'
    args = {}
    return render(request, page, args)


def cam_mic_new(request, page):
    page = 'cam_mic_new_' + page + '.html'
    args = {}
    return render(request, page, args)


def cam_mic_returning(request, page):
    page = 'cam_mic_returning_' + page + '.html'
    args = {}
    return render(request, page, args)
