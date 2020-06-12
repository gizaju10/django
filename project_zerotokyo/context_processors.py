from django.db.models import Count, Q

from blog.models import Category, Tag

from django.conf import settings


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'tags': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
    }
    return context

def site_common_text(request):
    return {'GOOGLE_MAP_API': settings.GOOGLE_MAP_API}