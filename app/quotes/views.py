import json

from django.db.models.aggregates import Count
from django.shortcuts import render
from taggit.models import Tag
from django.utils import timezone
from datetime import timedelta


from .models import PostModel, Visit


def index(request, selected_category=None):
    Visit.objects.create(
        page_name='INDEX',
        # date=(timezone.now() - timedelta(days=1))
    )

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
    Visit.objects.create(page_name='STATS')
    months = [
        "Jan.", "Feb.", "Mar.", "Apr", "May",
        "June", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."
    ]

    visits = Visit.objects.filter(date__gte=(timezone.now() - timedelta(days=7))).order_by('date')
    visits_data_by_date = {}
    for visit in visits:
        key = visit.date.strftime('%d/%m/%Y')
        if key not in visits_data_by_date:
            visits_data_by_date[key] = 1
        else:
            visits_data_by_date[key] += 1

    visits_data_by_name = {}
    for visit in visits:
        key = visit.page_name
        if key not in visits_data_by_name:
            visits_data_by_name[key] = 1
        else:
            visits_data_by_name[key] += 1

    visits_data_by_day_of_the_week = {}
    for visit in visits:
        key = visit.date.weekday()
        if key not in visits_data_by_day_of_the_week:
            visits_data_by_day_of_the_week[key] = 1
        else:
            visits_data_by_day_of_the_week[key] += 1

    tags = Tag.objects.all().annotate(
        num_times=Count('postmodel')
    )

    image_posts_with_alt_data = {
        'yes': len(PostModel.objects.filter(image__exact='', image_alt__isnull=False)),
        'no': len(PostModel.objects.filter(image__exact='', image_alt__isnull=True)),
    }

    videos_with_text_description_data = {
        'yes': len(PostModel.objects.filter(iframe__isnull=False, text__isnull=False)),
        'no': len(PostModel.objects.filter(iframe__isnull=False, text__isnull=True)),
    }

    context = {
        'active_users_names': json.dumps(list(visits_data_by_date.keys())),
        'active_users_count': json.dumps(list(visits_data_by_date.values())),

        'visits_day_of_the_week_names': json.dumps(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']),
        'visits_day_of_the_week_count': json.dumps([
            visits_data_by_day_of_the_week.get(0) or 0,
            visits_data_by_day_of_the_week.get(1) or 0,
            visits_data_by_day_of_the_week.get(2) or 0,
            visits_data_by_day_of_the_week.get(3) or 0,
            visits_data_by_day_of_the_week.get(4) or 0,
            visits_data_by_day_of_the_week.get(5) or 0,
            visits_data_by_day_of_the_week.get(6) or 0,
        ]),

        'posts_categories_names': json.dumps([tag.name for tag in tags]),
        'posts_categories_count': json.dumps([tag.num_times for tag in tags]),

        'image_posts_with_alt_names': json.dumps(list(image_posts_with_alt_data.keys())),
        'image_posts_with_alt_count': json.dumps(list(image_posts_with_alt_data.values())),

        'videos_with_text_description_names': json.dumps(list(videos_with_text_description_data.keys())),
        'videos_with_text_description_count': json.dumps(list(videos_with_text_description_data.values())),

        'loaded_page_names_names': json.dumps(list(visits_data_by_name.keys())),
        'loaded_page_names_count': json.dumps(list(visits_data_by_name.values())),
    }
    return render(request, 'stats.html', context)
