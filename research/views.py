from urllib import response

from celery.result import AsyncResult
from config.tasks import execute_long_task
from django.http import JsonResponse
from django.shortcuts import render

from research.models import Conversion


def test_view(request):
    conversion = Conversion(input="今日は良い天気だ")
    conversion.save()

    task_id = execute_long_task.delay(conversion.id)
    result = AsyncResult(task_id)

    print('result:', result, ' : ', result.state, ' : ', result.ready())

    response = {
        'progress': conversion.progress,
        'is_finished': conversion.is_finished,
    }
    response['id'] = conversion.id
    response['input'] = conversion.input
    response['output'] = conversion.output
    response['new_url'] = f"{request.scheme}://{request.get_host()}/conversions/"
    response['progress_url'] = f"{request.scheme}://{request.get_host()}/conversions/{conversion.id}/progress/"
    response['detail_url'] = f"{request.scheme}://{request.get_host()}/conversions/{conversion.id}/"
    return render(request, 'test.html', response)
    return JsonResponse(response)


def detail_view(request, pk):
    conversion = Conversion.objects.get(id=pk)

    response = {
        'progress': conversion.progress,
        'is_finished': conversion.is_finished,
    }
    response['id'] = conversion.id
    response['input'] = conversion.input
    response['output'] = conversion.output
    response['new_url'] = f"{request.scheme}://{request.get_host()}/conversions/"
    response['progress_url'] = f"{request.scheme}://{request.get_host()}/conversions/{conversion.id}/progress/"
    response['detail_url'] = f"{request.scheme}://{request.get_host()}/conversions/{conversion.id}/"
    return render(request, 'result.html', response)
    return JsonResponse(response)


def progress_view(request, pk):
    print(pk)
    conversion = Conversion.objects.get(id=pk)
    response = {
        'progress': conversion.progress,
        'is_finished': conversion.is_finished,
    }
    return JsonResponse(response)
