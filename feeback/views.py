from django.shortcuts import render, redirect

# Create your views here.
# def feedback(request):
#     return render(request, 'feedback/feedback.html')
from feeback.forms import feedform

def thankyou(request):
    return render(request, 'feedback/feedbackdone.html')

def feedback(request):
    form = feedform(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('feedback:thankyou',)
    return render(request,'feedback/feedback.html', {'form':form})