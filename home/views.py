from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request,mk):
    dict={
        'Name':'Mehedy Hasan Piale',
        'Marks':int(mk),
        'Courses':['CSE 303','HSS 301','CSE 311','CSE 312'],
        'CGPA':3.44

    }
    context=dict
    return render(request,'test.html',context)
def login_view(request):
    return render(request,'LogIn.html')
def home_page_view(request):
    return render(request,'home.html')
def registrar(request):
    return HttpResponse('<h1>Registration</h1>')
def doctors(request):
    return HttpResponse('<h1>Doctors</h1>')