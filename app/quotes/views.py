import json

from django.db.models.aggregates import Count
from django.shortcuts import render
from taggit.models import Tag

from .models import PostModel
import random

def index(request, selected_category=None):
    posts = PostModel.objects.all()
    if selected_category:
        posts = PostModel.objects.filter(tags__name=selected_category)
    context = {
        'posts': posts,
        'tags': Tag.objects.all(),
        'selected_category': selected_category
    }
    return render(request, 'index.html', context)


def stats(request):
    tags = Tag.objects.all().annotate(
        num_times=Count('postmodel')
    )

    context = {
        'active_users_names': json.dumps(
            [
                "Jan.", "Feb.", "Mar.", "Apr", "May",
                "June", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."
            ]
        ),
        'active_users_count': json.dumps([
            random.randint(0, x) + 30 for x in range(12)
        ]),

        'posts_categories_names': json.dumps([tag.name for tag in tags]),
        'posts_categories_count': json.dumps([tag.num_times for tag in tags]),

        'genders_platform_names': json.dumps(['Male', 'Female', 'Other']),
        'genders_platform_count': json.dumps([62, 33, 5]),
    }
    return render(request, 'stats.html', context)
