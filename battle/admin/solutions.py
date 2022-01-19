from django.contrib.admin import (
    ModelAdmin,
    register,
)

from battle.models import Solution


@register(Solution)
class SolutionModelAdmin(ModelAdmin):
    fields = (
        'user',
        'problem',
        'code',
        'lang',
        'result',
        'judge_id',
        'test_count',
        'created',
        'modified',
    )
    list_display = (
        'user',
        'judge_id',
        'problem',
        'lang',
        'result',
        'test_count',
    )
    list_display_links = (
        'judge_id',
    )
    readonly_fields = (
        'judge_id',
        'result',
        'test_count',
        'created',
        'modified',
    )
