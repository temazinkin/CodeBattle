from django.urls import (
    path,
)

from battle.views import check_solution

urlpatterns = [
    path('result/<int:solution_id>', check_solution, name='result'),
]
