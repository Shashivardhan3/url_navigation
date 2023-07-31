from django.shortcuts import render

# Create your views here.


def python(request):
    d={'name':'shashi','age':24,'hobbies':['cricket','football','hockey']}
    return render (request,'python.html',context=d)

def django(request):
    d={'a':24,'b':56,'c':148}
    return render (request,'django.html',context=d)