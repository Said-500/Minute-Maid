from django.shortcuts import render,redirect
from .models import NewModel
def Home(request):
    user_data =NewModel.objects.all()
    print(user_data)
    print(user_data.values())
    return render(request,'Home.html',{'user_details;':user_data})
    
def Signup(request):
    print(request.method)
    if request.method =='POST':
        print(request.POST)
        name = request.POST.get('username')
        user_email = request.POST.get('email')
        user_age = request.POST.get('age')
        user_password = request.POST.get('password')
        user_obj = NewModel()
        user_obj.username = name
        user_obj.email = user_email
        user_obj.age = user_age
        user_obj.password = user_password
        user_obj.save()
        return redirect('/')
    return render(request,'Signup.html')
def about(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'contactus.html')
def edit(request,id):
    userapp =NewModel.objects.get(id =id)

    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        user_email = request.POST.get('email')
        user_age = request.POST.get('age')
        user_password = request.POST.get('password')
        userapp.username = name
        userapp.email = user_email
        userapp.age = user_age
        userapp.password = user_password
        userapp.save()
        return redirect('/')
    return render(request,'edit.html',{'user': userapp})

def delete(request,id):
    userapp = NewModel.objects.get(id=id)
    userapp.delete()
    print(f'id {id} deleted')
    return redirect('/')