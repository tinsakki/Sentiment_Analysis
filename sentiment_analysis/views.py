from django.shortcuts import render
from textblob import TextBlob

def homepage(request):
    return render(request, 'home.html')

def prediction(request):
    ans = ''
    if request.method == 'POST':
        comment = request.POST['comment']
        analysis = TextBlob(comment)
        if analysis.sentiment[0] > 0:
            ans = 'Positive'
        elif analysis.sentiment[0] < 0:
            ans = 'Negative'
        else:
            ans = 'Neutral'
    return render(request,'prediction.html',context={"result":ans})

		
	


