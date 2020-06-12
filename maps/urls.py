from django.urls import path
from .views import mapfunc, tokyofunc, tagfunc, tokyo23func

from . import views


app_name = 'maps'
urlpatterns = [
    path('map/', mapfunc, name="map"),
    path('tokyo23/', tokyo23func, name="tokyo23"),
    path('tag/', tagfunc, name="tag"),
    path('tokyo/', tokyofunc, name="tokyo"),
    # path('chiyoda/', chiyodafunc),
    # path('chuo/', chuofunc),
    
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]