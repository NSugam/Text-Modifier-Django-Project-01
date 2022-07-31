# File Created By Me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def analyze(request):
    text_area = request.POST.get('text_area', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalfirst_all = request.POST.get('capitalfirst_all', 'off')
    capitalall = request.POST.get('capitalall', 'off')

    if removepunc == "on":
        params2 = {'purpose': 'Removed Punctuations'}
        analyzed = ""
        if text_area != "":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in text_area:
                if char not in punctuations:
                    analyzed = analyzed + char
                    params2 = {'purpose': 'Removed Punctuations'}    
            text_area = analyzed

    if capitalfirst_all == "on":
        analyzed = ""
        analyzed = analyzed + text_area.title()
        params2 = {'purpose': 'Capital first letters'}
        text_area = analyzed

    if capitalall == "on":
        analyzed = ""
        analyzed = analyzed + text_area.upper()
        params2 = {'purpose': 'Capital All Words'}
        text_area = analyzed

    if (removepunc != "on" and capitalfirst_all != "on" and capitalall != "on"):
        params = {'purpose': 'No option choosen'}
        return render(request, 'analyze.html', params)

    params = {'analyzed_text': analyzed}
    params.update(params2)

    return render(request, 'analyze.html', params)
