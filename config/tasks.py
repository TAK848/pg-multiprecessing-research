import time

from celery import shared_task


@shared_task
def add(x1, x2):
    time.sleep(10)
    y = x1 + x2
    print('処理完了')
    return y
