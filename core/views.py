from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile


def home(request):
    return render(request, 'core/home.html')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Sua conta foi atualizada!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'core/profile.html', context)

def search(request, city='', value=''):
    if value:
        result = Profile.objects.filter(city=city, services=value)
    else:
        result = Profile.objects.all().filter(city=city)
        print(result)

    context = {
        'result': result
    }

    return render(request, 'core/search_result.html', context)