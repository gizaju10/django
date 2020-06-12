from django.contrib import admin
from django.urls import path, include
# メディアファイルを利用
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', include('maps.urls')),
    path('accounts/', include('allauth.urls')),
    # 投稿、コメントの追加
    path('blog/', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)