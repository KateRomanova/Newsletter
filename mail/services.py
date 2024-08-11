from random import shuffle

from blog.models import Blog
from mail.models import Newsletter, Client


def get_three_articles():
    """Получает три случайных статьи из блога"""

    blog = list(Blog.objects.all())
    shuffle(blog)
    return blog[:3]



