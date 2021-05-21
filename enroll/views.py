from django.shortcuts import render, HttpResponseRedirect
from . forms import StudentRegistration
from django.contrib import messages
from . models import User
# Create your views here.

# This function will add new item and show all items
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pw)
            reg.save()
            messages.success(request, 'Congratulation !! you have registerted successfully')
            fm=StudentRegistration()
            
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit.
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Congratulation !! you have updated successfully')
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})  
    

# This Function will Delete
def delete_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'You have deleted one data successfully')
        return HttpResponseRedirect('/')
    

        
    