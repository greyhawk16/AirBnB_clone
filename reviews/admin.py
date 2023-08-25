from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = 'Filter By Words'
    parameter_name = 'BB-61'

    def lookups(self, request, model_admin):
        return [
            ('good', 'Good'),
            ('great', 'Great'),
            ('awsome', 'Awsome'),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'payload'
    )
    list_filter = (
        WordFilter,
        'rating',
        'user__is_host',
        'room__category',
        'room__pet_friendly',
    )
