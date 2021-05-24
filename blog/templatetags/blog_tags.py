from ..models import Post
from django import template
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def total_post():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_post(count=3):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_post}


@register.inclusion_tag('blog/post/commented_post.html')
def get_most_commented_posts(count=3):
    commented = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'commented': commented}


@register.filter(name="markdown")
def markdown_formatted(text):
    return mark_safe(markdown.markdown(text))

