from django.shortcuts import render

# Create your views here.
def leo(request):
    dict={'name':'sasi','nm':'charan'}
    return render(request,'generic.html',context=dict)