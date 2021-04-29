from django.shortcuts import render


def cam_mic_user_status(request):
    page = 'Cam_Mic_0.html'
    args = {}
    return render(request, page, args)

def cam_mic_user_status1(request):
    page = 'Cam_Mic_1.html'
    args = {}
    return render(request, page, args)
    
def cam_mic_user_status2(request):
    page = 'Cam_Mic_2.html'
    args = {}
    return render(request, page, args)
    
def cam_mic_user_status3(request):
    page = 'Cam_Mic_3.html'
    args = {}
    return render(request, page, args)

def cam_mic_new(request):
    page = 'cam_mic_new_' + page + '.html'
    args = {}
    return render(request, page, args)


def cam_mic_returning(request, page):
    page = 'cam_mic_returning_' + page + '.html'
    args = {}
    return render(request, page, args)
