from blog.forms import SubscribeForm
from blog.models import PostTag, PostCategory


def users_and_projects(request):
    tags = PostTag.objects.all()
    categories = PostCategory.objects.all()
    return {'subscribe_form': SubscribeForm(),
            'tags': tags,
            'categories' : categories
            }