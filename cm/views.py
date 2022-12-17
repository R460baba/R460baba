from django.shortcuts import render
from .models import student
from .forms import user
def base(request):
    return render(request,'base.html')

def students(request):
    if request.method=='POST':
        form=user(request.POST)
        if form.is_valid():
            form.save()
            form=user()
            return render(request, 'baseform.html',{'form':form,'msg':"success"})
    else:
        form=user()
        return render(request, 'baseform.html',{'form':form ,'msg':"not success"})

def use(request):
    data=student.objects.all()
    return render(request, 'database.html',{'data':data,'msg':"success"})
