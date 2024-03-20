from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from users.forms import LoginUserForm, RegisterUserForm
from django.contrib import messages


# Create your views here.

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = LoginUserForm
    template_name = 'users/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')

    # def form_invalid(self, form):
    #     messages.error(self.request, 'Invalid username or password')
    #     return self.render_to_response(self.get_context_data(form=form_class))


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
