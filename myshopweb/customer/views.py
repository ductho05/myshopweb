from django.views import generic
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import cache_control,never_cache
from .models import User
from .forms import  RegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import django.contrib.messages as messages


# Create your views here.

# Views đăng kí
def Register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,"register.html",{'form':form})
    

decorators = [never_cache,]
@method_decorator(decorators, name='dispatch')
class ProfileView(generic.ListView):
    model = User
    context_object_name = 'user'
    template_name = 'profile.html'
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        return render(request,'profile.html')
    
    def post(self,request, *args, **kw):
        data = request.POST      
          
        User.objects.filter(email=data['email']).update(full_name =data['full_name']
        ,phone_number=data['phone_number'],date =data['date'],address=data['address'])
        return render(request,'profile.html')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


decorators = [never_cache, login_required(login_url='/')]
@method_decorator(decorators, name='dispatch')
class PasswordChangeView(generic.ListView):
    model = User
    context_object_name = 'user_password'
    template_name = 'password_change.html'
    queryset = User.objects.all()    
    def post(self,request, *args, **kw):
            data = request.POST
            current_user = request.user
            u = User.objects.get(email = current_user.email)
            u_password =User.objects.filter(email = current_user.email)
            if current_user.is_authenticated:
                if(data['new_password'] == data ['new_password_again']):       
                    if(u.check_password(data['old_password'])):
                        new_password = make_password(data['new_password'])                
                        print(current_user.password)
                        u_password.update(password=new_password)
                        return render(request,'password_change_done.html')
                    else:
                        messages.error(request, 'Sai mật khẩu!')
                        return render(request,'password_change.html')
                else:
                    messages.error(request, 'Không khớp!')
                    return render(request,'password_change.html')
            else:
                return redirect('/')
    def __str__(self):
        return self.username

decorators = [never_cache]
@method_decorator(decorators, name='dispatch')
class MyLoginView(LoginView):
    model = User
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Sai tài khoản hoặc mật khẩu!')
                return render(request,'login.html')
        else:
            return render(request,'login.html')

# @login_required
# def profile(request):
#     UserEditForm = modelform_factory(
#         User, fields=('full_name','phone_number', 'address','date'))
#     form = UserEditForm(instance=request.user)
#     if request.method == "POST":
#         form = UserEditForm(instance=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'profile.html',{'form':form})