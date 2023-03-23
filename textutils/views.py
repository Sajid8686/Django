from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')
    
    #**************** To remove punctuations ******************************
    
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
                
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    #*************************** To capitalize **********************
    
    elif(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {'purpose':'Change to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #************************** To remove new line *****************************
    
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed= analyzed + char
                
        params = {'purpose':'Remove New line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #************************** To remove Extra spaces *****************************
    
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed= analyzed + char
                
        params = {'purpose':'Remove Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #************************** To Count Characters *****************************
    
    elif(countchar == "on"):
        analyzed=""
        for char in djtext:
            analyzed = len(djtext)
            
        params = {'purpose':'Count Characters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Error")
    
