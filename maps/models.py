from django.db import models

# 記事に使用しない画像のアップロード時に使用
class ImagesModel(models.Model):
    images = models.ImageField(upload_to='')