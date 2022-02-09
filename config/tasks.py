from time import sleep

from django.utils import timezone
from research.models import Conversion

from celery import shared_task


@shared_task
def execute_long_task(id):
    print('タスクに入った')
    print(f'id: {id}')
    conversion = Conversion.objects.get(id=id)
    for i in range(1000):
        conversion.progress = i / 10
        conversion.save()
        sleep(0.01)
    conversion.progress = 100
    conversion.output = "本日は良い天気であります"
    conversion.converted_at = timezone.now()
    conversion.is_finished = True
    conversion.save()
