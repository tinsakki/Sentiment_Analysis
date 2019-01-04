from django.shortcuts import render
from django.http import JsonResponse

from textblob import TextBlob
def prediction(request):
    ans = ''
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginners pit.
        if request.is_ajax():
            email = request.POST.get('email')
            analysis = TextBlob(email)
            if analysis.sentiment[0] > 0:
                ans = 'Positive'
            elif analysis.sentiment[0] < 0:
                ans = 'Negative'
            else:
                ans = 'Neutral'

            data = {"email":ans}
            return JsonResponse(data)
    #Get goes here
    return render(request,'prediction.html')