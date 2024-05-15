from django.shortcuts import render
from .models import Student
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')

def registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    Cpassword=request.POST.get('Cpassword')
    data=Student.objects.filter(Email=email)
    print(data)
    if data:
        msg='Already Email Exist'
        return render(request,'register.html',{'key':msg})
    else:
        if password==Cpassword:
            Student.objects.create(Name=name,
                               Email=email,
                               Password=password)
            msg="Register successfully"
            return render(request,'login.html',{'key':msg})
        
        else:
            msg="password and confirm password not matched"
            return render(request,'register.html',{'key':msg})

def logindata(request):
    # print(request.method)
    # print(request.POST)
    email=request.POST.get('email')
    pswrd=int(request.POST.get('password'))
    user=Student.objects.filter(Email=email)
    if user:
        data=Student.objects.get(Email=email)
        pss=data.Password
        print(pss)
        print(pswrd)
        if pss == pswrd:
            print(pswrd)
            context={
               'nm':data.Name,
               'em':data.Email,
               'logout':'logout',
            } 
            return render(request,'dashboard.html',{'context':context})
        else:
            msg="Email and Password not matched"
            return render(request,'login.html',{'key':msg})
    else:
        msg="Enter valid EmailId"
        return render(request,'login.html',{'key':msg})
    
def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    return render(request,'home.html')
    
        

        
        
     

