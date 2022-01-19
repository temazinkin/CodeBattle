from django.contrib.admin import (
    ModelAdmin,
    register,
)

from battle.models import Problem


@register(Problem)
class ProblemModelAdmin(ModelAdmin):
    fields = (
        'level',
        'problem',
        'short_name',
        'contest_id',
        'created',
        'modified',
    )
    list_display = (
        'id',
        'short_name',
        'level',
        'contest_id',
    )
    list_display_links = (
        'id',
        'short_name',
    )
    ordering = (
        'level',
        'pk',
    )
    readonly_fields = (
        'created',
        'modified',
    )
