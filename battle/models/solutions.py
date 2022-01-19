from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CASCADE,
    SET_NULL,
    CharField,
    TextField,
    ForeignKey,
    PositiveSmallIntegerField,
    DateTimeField,
)

from battle.models import Problem


class Solution(Model):
    LANGS = (
        ('python3', 'Python 3'),
        ('g++', 'C++'),
    )
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='пользователь',
    )
    judge_id = PositiveSmallIntegerField(
        'judge_id',
        editable=False,
        blank=True,
        null=True,
    )
    problem = ForeignKey(
        Problem,
        on_delete=SET_NULL,
        verbose_name='задача',
        null=True,
        blank=True,
    )
    code = TextField(
        'решение задачи',
    )
    lang = CharField(
        'язык программирования',
        choices=LANGS,
        max_length=15,
    )
    result = CharField(
        'результат проверки',
        editable=False,
        blank=True,
        null=True,
        max_length=10,
    )
    test_count = PositiveSmallIntegerField(
        'количество успешных тестов',
        editable=False,
        blank=True,
        null=True,
    )
    created = DateTimeField(
        'создано',
        auto_now_add=True,
    )
    modified = DateTimeField(
        'обновлено',
        auto_now=True,
    )

    def __str__(self):
        if self.result:
            return f'{self.user.username} — {self.result}'
        return f'{self.user.username} — проверяется'

    class Meta:
        db_table = 'solutions'
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
        ordering = (
            '-modified',
        )
