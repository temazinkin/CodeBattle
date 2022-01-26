from django.shortcuts import render, get_object_or_404

from battle.models import Solution
from battle.services.check_system import (
    request_result,
    request_judge_id,
)


def check_solution(request, solution_id):
    solution = get_object_or_404(
        Solution,
        id=solution_id,
    )
    if not solution.result and solution.judge_id:
        data = {
            'ParcelID': solution.id,
            'RunID': solution.judge_id,
            'ContestID': solution.problem.contest_id,
        }
        result = request_result(data)
        if result:
            status, tests = result
            solution.result = status
            solution.test_count = tests
            solution.save()

    if not solution.judge_id:
        data = {
            'ParcelID': solution.id,
            'CodeContent': solution.code,
            'ContestID': solution.problem.contest_id,
            'ProblemShortName': solution.problem.short_name,
            'LanguageShortName': solution.lang,
        }
        judge_id = request_judge_id(data)
        if judge_id:
            solution.judge_id = judge_id
            solution.save()

    context = {
        'title': 'Результат',
        'solution': solution,
    }
    return render(request, 'solution/check.html', context=context)
