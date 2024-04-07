from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,LoginForm, BaseUserCandidateForm, AdminUserCandidateForm
from django.contrib.auth import authenticate, login, logout
from .models import Candidate

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('login')
        else:
            msg = 'Form is not valid.'
    else:
        form = SignUpForm()
        
    return render(request,'register.html',{'form':form,'msg':msg})

def user_login(request):
    msg = None
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.role == 'admin':
                login(request, user)
                return redirect('home_admin')
            elif user is not None and user.role == 'base':
                login(request, user)
                return redirect('home_base')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'Error validating form.'
    return render(request, 'login.html', {'form': form, 'msg': msg})
        


def user_logout(request):
    logout(request)
    return redirect('index')

def home_admin(request):
    return render(request, 'home_admin.html')

def home_base(request):
    if request.method == 'POST':
        form = BaseUserCandidateForm(request.POST)
        if form.is_valid():
           
            form.save()
           
            return redirect('success') 
    else:
        
        form = BaseUserCandidateForm(initial={'decision': 'No'})
    
    return render(request, 'home_base.html', {'form': form})

def home_admin(request):
    if request.method == 'POST':
        form = AdminUserCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_admin')
    else:
        form = AdminUserCandidateForm()
    candidates = Candidate.objects.filter(status='awaiting permission')
    return render(request, 'home_admin.html', {'candidates': candidates,'form':form})

def success(request):
    return render(request, 'success.html')

def success_admin(request):
    return render(request,'success_admin.html')

def modify_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    
    if request.user.role == 'admin':
        form_class = AdminUserCandidateForm
    else:
        form_class = BaseUserCandidateForm
    
    if request.method == 'POST':
        form = form_class(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('home_admin')  
    else:
        form = form_class(instance=candidate)
        
    return render(request, 'modify_permission.html', {'form': form, 'candidate': candidate})

def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate,id=candidate_id)
    candidate.delete()
    return redirect('home_admin')

