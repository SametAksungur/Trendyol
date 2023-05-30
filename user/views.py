from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def userRegister(request):
    if request.method == 'POST':
        kullaniciAdi = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            if User.objects.filter(username=kullaniciAdi).exists():
                messages.error(request, 'Kullanıcı adı kullanılıyor')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email kullanımda')
                return redirect('register')
            elif len(sifre1) < 6:
                messages.error(
                    request, 'Şifre en az 6 karakter olması gerekiyor')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=kullaniciAdi,
                    email=email,
                    password=sifre1
                )

                user.save()
                messages.success(request, 'Kayıt başarılı')
                return redirect('index')
        else:
            messages.error(request, 'Şifreler uyuşmuyor')
            return redirect('register')

    return render(request, 'register.html')


def userLogin(request):
    if request.method == 'POST':

        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username=kullanici, password=sifre)
        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Başarılı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'login.html')


def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')
