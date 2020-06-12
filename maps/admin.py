from django.contrib import admin
from .models import ImagesModel
# Register your models here.

# modelsを管理画面で使う際、必須
admin.site.register(ImagesModel)