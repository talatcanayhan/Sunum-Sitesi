from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
from .models import Message

def home(request):
    comments = Message.objects.all()
    context = {'comments': comments}
    return render(request, 'sunumapp/anasayfa.html', context)


def sayfa1(request):
    return render(request, 'sunumapp/sayfa1.html')

def sayfa2(request):
    return render(request, 'sunumapp/sayfa2.html')

def sayfa3(request):
    context={}
    context['form'] = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, 'sunumapp/sayfa3.html',context)



