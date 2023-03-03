from django.db import models

import email

# Create your models here.


class Brands(models.Model):
    brend = models.CharField('brend',max_length = 14)
    user_id = models.IntegerField('user_id',default=2)
    image = models.FileField(upload_to = 'images',default='https://archive.org/download/no-photo-available/no-photo-available.png')
    data_brend = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brend

class Clients(models.Model):
    ad = models.CharField('ad',max_length = 14)
    imageclient = models.FileField(upload_to = 'images',default='https://archive.org/download/no-photo-available/no-photo-available.png')
    soyad = models.CharField('soyad',max_length = 20)
    tel = models.CharField('tel',max_length = 20)
    email = models.CharField('email',max_length = 50)
    shirket = models.CharField('shirket',max_length = 35)
    user_id = models.IntegerField('user_id',default=2)
    data_client = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad

class Products(models.Model):
    mehsul = models.CharField('mehsul',max_length = 35)
    imageproduct = models.FileField(upload_to = 'images',default='https://archive.org/download/no-photo-available/no-photo-available.png')
    alis = models.IntegerField('alis')
    satis = models.IntegerField('satis')
    miqdar = models.IntegerField('miqdar')
    brand_id = models.ForeignKey(Brands,on_delete = models.CASCADE)
    user_id = models.IntegerField('user_id',default=2)
    data_product = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mehsul

class Orders(models.Model):
    pmiqdar = models.IntegerField('pmiqdar')
    client_id = models.ForeignKey(Clients,on_delete = models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Products,on_delete = models.CASCADE,)
    user_id = models.IntegerField('user_id',default=2)
    
    data_order = models.DateTimeField(auto_now_add=True)

    tesdiq = models.IntegerField('tesdiq')

   

class Expenses(models.Model):
    xerc = models.IntegerField('xerc')
    user_id = models.IntegerField('user_id',default=2)
    data_xerc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.xerc


class Ishciler(models.Model):
    ad = models.CharField('ad',max_length = 35)
    soyad = models.CharField('soyad',max_length = 35)
    telefon = models.CharField('telefon',max_length = 35)
    ev_tel = models.CharField('ev_tel',max_length = 35)
    unvan = models.CharField('unvan',max_length = 35)
    email = models.CharField('email',max_length = 35)
    vezife = models.CharField('vezife',max_length = 35)
    user_id = models.IntegerField('user_id')
    data_ishciler = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad


class Senedler(models.Model):
    ishci_id= models.IntegerField('ishci_id',max_length = 35)
    basliq = models.CharField('basliq',max_length = 35)
    skan = models.FileField(upload_to = 'images',default='https://archive.org/download/no-photo-available/no-photo-available.png')
    qeyd = models.CharField('qeyd',max_length = 35)

    data_senedler = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qeyd