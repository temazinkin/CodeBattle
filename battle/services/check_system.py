import os
import requests


def request_to_check_system(data: dict) -> str:
    ''' Выполняет запрос к тестирующей системе '''
    url = os.getenv('CHECK_SYSTEM')
    data['SessionKey'] = data.get('SessionKey', os.getenv('CHECK_API'))
    try:
        response = requests.post(
            url,
            data=data,
        )
        if response.status_code == 200:
                return response.text
    except Exception as e:
            print(e, data)
            return ''


def request_judge_id(data: dict) -> int:
    ''' Запрашиваем judge_id от тестирующей системы '''
    data['ActionNature'] = 'SubmitRun'
    response_judge_id = request_to_check_system(data)
    if response_judge_id:
        judge_id = int(response_judge_id.splitlines()[-1])
        return judge_id
