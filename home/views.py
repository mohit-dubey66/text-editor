from typing import Text
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):

    

    return render(request,'index.html')

def analyzed(request):
    text = request.GET.get('text')
    removepunc = request.GET.get('removepunc','off')
    capitalise = request.GET.get('capitalise','off')
    listOfPunctations = '''.?!,;:-_()[]{'"}*&^%@#$+='''
    print(text)
    print(removepunc)
    analyzedData = ""
    if removepunc == 'on':
        for char in text:
            if char not in listOfPunctations:
                analyzedData+= char
    
    
    if(capitalise == 'on'):
        for char in text:
            up = char.upper()
            analyzedData = analyzedData + up

    else:
        return HttpResponse("Invalid Creds")
    context = {'purpose':"Capitalised Characters",'data':analyzedData}
            
        
    
    return render(request,'result.html',context)