from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    pengguna = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=50, default='', blank=True)
    gambar = models.ImageField(default='default.jpeg', upload_to='profil_img', blank=True)
    tentang = models.TextField(max_length=100, default='silahkan deskripsikan tentang diri anda!!', blank=True)
    alamat = models.CharField(max_length=100, default='', blank=True)
    website = models.CharField(max_length=30, default='', blank=True)
    hp = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.pengguna}'

    # Ketika ingin mengganti metode penyimpana .save() model Django harus menambahkan parameter *args dan **kwargs ke metode yang ditimpa
    def save(self, *args, **kwargs):
        super(Profil, self).save(*args, **kwargs)

        img = Image.open(self.gambar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.gambar.path)
