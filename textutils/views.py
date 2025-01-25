from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')

    # Initialize variables
    analyzed = djtext
    purpose_list = []

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        purpose_list.append("Removed Punctuations")

    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose_list.append("Changed to Uppercase")

    if newlineremover == "on":
        analyzed = " ".join(char for char in analyzed if char not in ["\n", "\r"])
        purpose_list.append("Removed New Lines")

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        purpose_list.append("Removed Extra Spaces")

    if countchar == "on":
        char_count = len(analyzed)
        purpose_list.append(f"Counted Characters ({char_count})")
        analyzed = f"Character Count: {char_count}"

    # Handle no operations selected
    if not purpose_list:
        return HttpResponse("Error: No operation selected. Please select at least one operation.")

    # Prepare context for rendering
    context = {
        'purpose': ", ".join(purpose_list),
        'analyzed_text': analyzed,
        'original_text': djtext
    }
    return render(request, 'index.html', context)
