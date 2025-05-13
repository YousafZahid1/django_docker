from celery import shared_task
from django.utils import timezone
from .models import BlogPost

@shared_task
def update_blog_dates():
    """Update the last_updated_date field of all blog posts to the current date."""
    current_date = timezone.now().date()
    BlogPost.objects.all().update(last_updated_date=current_date)
    return f"Updated {BlogPost.objects.count()} blog posts to date {current_date}" 