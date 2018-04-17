from django.shortcuts import render


def alertRender(request, message=None, target=None):
    params = {}
    if message is not None:
        params["message"] = message
    if target is not None:
        params["location"] = target
    return render(request, 'alert.html', params)