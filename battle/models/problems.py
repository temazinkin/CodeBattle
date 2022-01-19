from django.db.models import (
    Model,
    CharField,
    TextField,
    PositiveSmallIntegerField,
    DateTimeField,
)


class Problem(Model):
    LEVEL = (
        ('easy', 'Легкий'),
        ('normal', 'Нормальный'),
        ('hard', 'Сложный'),
    )
    level = CharField(
        'уровень сложности',
        max_length=10,
        choices=LEVEL,
    )
    problem = TextField(
        'условие задачи',
    )
    short_name = CharField(
        'short_name',
        max_length=70,
    )
    contest_id = PositiveSmallIntegerField(
        'contest_id',
        default=9,
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
        return f'{self.level}: {self.short_name} {self.id}'

    class Meta:
        db_table = 'problems'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
