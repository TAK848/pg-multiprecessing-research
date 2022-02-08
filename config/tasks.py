import time
from datetime import datetime
from time import sleep

from django.utils import timezone
from research.models import Conversion

from celery import shared_task


@shared_task
def add(x1, x2):
    time.sleep(1)
    y = x1 + x2
    print('処理完了')
    return y


@shared_task
def execute_long_task(id):
    print('プロセスに入った')
    print(f'id: {id}')
    # return 0
    # print(Conversion.objects.all())
    conversion = Conversion.objects.get(id=id)
    for i in range(10):
        conversion.progress = i * 10
        conversion.save()
        # conversion.
        sleep(1)
    conversion.output = "本日は良い天気であります"
    conversion.converted_at = timezone.now()
    conversion.is_finished = True
    conversion.save()

    # time.sleep(10)
    # y = x1 + x2
    # print('処理完了')
    # return y
