from django.shortcuts import render

# Create your views here.
def das(request):
    dict={'name':'charan'}
    return render(request,'generic.html',context=dict)