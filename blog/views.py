from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from .models import Post

class DaftarBlog(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    # mengurutkan dari urutan publikasi dari belakang
    ordering = ['-publikasi']
    # membuat paginet dengan 3 bangian
    paginate_by = 3

class DaftarPenggunaBlog(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'post'
    # mengurutkan dari urutan publikasi dari belakang
    ordering = ['-publikasi']
    # membuat paginet dengan 3 bangian
    paginate_by = 5

    def get_query_set(self):
        user = get_object_or_404(User, pengguna=self.kwargs.get('pengguna'))
        return Post.object.filter(penulis=user).order_by('-publikasi')

class DetailBlog(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BuatBlog(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['judul', 'konten']
    # Membuat logika untuk tombol posting
    def form_valid(self, form):
        # user mencoba untuk mengirimkan sebuah request (file konten) sebelum user melakukan  itu akan dicatat sebagai pengguna akhir saat ini dan setelah itudjango baru dapat memvalidasi file/request tsb.
        form.instance.penulis = self.request.user
        return super().form_valid(form)

class EditBlog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['judul', 'konten']
    # Membuat logika untuk tombol posting
    def form_valid(self, form):
        # user mencoba untuk mengirimkan sebuah request (file konten) sebelum user melakukan  itu akan dicatat sebagai pengguna akhir saat ini dan setelah itudjango baru dapat memvalidasi file/request tsb.
        form.instance.penulis = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.penulis:
            return True
        return False

class HapusBlog(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.penulis:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'judul': 'About'})
