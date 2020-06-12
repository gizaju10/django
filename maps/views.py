import logging

from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import InquiryForm

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('maps:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


# Create your views here.

def mapfunc(request):
    return render(request, 'map.html')

def tokyo23func(request):
    return render(request, 'tokyo23.html')

def tagfunc(request):
    return render(request, 'tag.html')

def tokyofunc(request):
    return render(request, 'tokyo.html')

# def chiyodafunc(request):
#     return render(request, 'tokyo23_1_chiyoda.html', {'some':100})

# def chuofunc(request):
#     return render(request, 'tokyo23_2_chuo.html', {'some':100})