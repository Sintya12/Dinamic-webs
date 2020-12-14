from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegisterPengguna, UpdatePengguna, UpdateProfile

def register(request):
    if request.method == 'POST':
        form = RegisterPengguna(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Berhasil membuat akun {username}, silahkan login!')
            return redirect('login')

    else:
        form = RegisterPengguna()

    return render(request, 'akun/register.html', {'form': form})

# akan menampilkan menu profil hanya apabila user berstatus login
@login_required
def profil(request, user):
    if request.method == 'POST':
        uform = UpdatePengguna(request.POST, instance=request.user)
        pform = UpdateProfile(request.POST,
                              request.FILES,
                              instance=request.user.profil)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Profil berhasil diperbarui!')
            return redirect(reverse('profil', kwargs={'user': request.user}))
    else:
        uform = UpdatePengguna(instance=request.user)
        pform = UpdateProfile(instance=request.user.profil)

    context = {
        'uform': uform,
        'pform': pform,
    }
    return render(request, 'akun/profil.html', context)
