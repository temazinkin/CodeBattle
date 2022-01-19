from django.shortcuts import render


def github_login(request):
    context = {
        'title': 'Code Battle',
    }
    return render(request, 'account/github_login.html', context=context)


def profile_page(request):
    context = {
        'title': 'Профиль',
    }
    return render(request, 'account/profile.html', context=context)
