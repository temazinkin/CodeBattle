import os

import requests
from django.shortcuts import render, get_object_or_404

from battle.models import Solution


def check_solution(request, solution_id):
    solution = get_object_or_404(
        Solution,
        id=solution_id,
    )
    if not solution.result and solution.judge_id:
        try:
            request_result = requests.post(
                os.getenv('CHECK_SYSTEM'),
                data={
                    'SessionKey': os.getenv('CHECK_API'),
                    'ActionNature': 'RunStatus',
                    'ParcelID': solution.id,
                    'RunID': solution.judge_id,
                    'ContestID': solution.problem.contest_id,
                }
            )
            if request_result.status_code == 200:
                result_all = request_result.text.splitlines()[-1].split(';')
                print(result_all)
                result = result_all[6]
                test_count = result_all[7]
                if result:
                    solution.result = result
                if test_count:
                    solution.test_count = int(test_count) - 1
                solution.save()
        except Exception as e:
            print('RunStatus', e)

    if not solution.judge_id:
        try:
            request_judge_id = requests.post(
                os.getenv('CHECK_SYSTEM'),
                data={
                    'SessionKey': os.getenv('CHECK_API'),
                    'ActionNature': 'SubmitRun',
                    'ParcelID': solution.id,
                    'CodeContent': solution.code,
                    'ContestID': solution.problem.contest_id,
                    'ProblemShortName': solution.problem.short_name,
                    'LanguageShortName': solution.lang,
                }
            )
            if request_judge_id.status_code == 200:
                judge_id = int(request_judge_id.text.splitlines()[-1])
                if judge_id:
                    solution.judge_id = judge_id
                    solution.save()
        except Exception as e:
            print('SubmitRun', e)

    context = {
        'title': 'Результат',
        'solution': solution,
    }
    return render(request, 'solution/check.html', context=context)
