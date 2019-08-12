from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Security/index.html')


def practice(request):
    return render(request, 'Security/Good_practices.html')


def malware(request):
    return render(request, 'Security/Malware.html')


def settings(request):
    return render(request, 'Security/Settings_changes.html')


def software(request):
    return render(request, 'Security/Software_Requirements.html')