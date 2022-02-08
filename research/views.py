import datetime
import multiprocessing as mp
import os
import uuid
from time import sleep

from config.tasks import add
from django.http import JsonResponse

from .models import Conversion

mp.set_start_method('fork')


# def create_another_process():

#     # プロセスIDを取得
#     pid = os.getpid()
#     print('process1:' + str(pid))

#     # サブプロセスを生成する
#     p = mp.Process(target=execute_long_process, args=(
#         "Message: call execute_anothoer_process()!", datetime.datetime.now()))
#     # p2 = mp.Process(target=execute_anothoer_process, args=(
#     #     "Message: call execute_anothoer_process()!",))
#     # p3 = mp.Process(target=execute_anothoer_process, args=(
#     #     "Message: call execute_anothoer_process()!",))

#     # サブプロセスを開始する
#     p.start()
#     # p2.start()
#     # p3.start()
#     return 'a'


def test_view(request):
    response = {}
    conversion = Conversion(input="今日は良い天気だ")
    conversion.save()
    print(conversion)
    # プロセスIDを取得
    pid = os.getpid()
    print(f'今のprocessID: {pid}')
    # サブプロセスを生成する
    print(str(conversion.id))
    a = str(conversion.id)
    # a = "Message: asafsfa"
    p = mp.Process(
        target=execute_long_process,
        args=[a],
    )
    print('process created')
    p.start()

    print('process started')
    # print(create_another_process())
    # print('a')
    # print('a')
    # conversion = Conversion.objects.get(id=a)
    # print(conversion)
    # print(f"txt: {conversion.input}")
    response['id'] = conversion.id
    response['input'] = conversion.input
    return JsonResponse(response)


def execute_long_process(id):

    print('プロセスに入った')
    # 元のプロセスから引き継いだ文字列を表示
    print(f'id: {id}')
    print(Conversion.objects.all())
    conversion = Conversion.objects.get(id=id)
    print(conversion)
    print(f"txt: {conversion.input}")

    # プロセスIDを取得
    pid = os.getpid()
    print(f'今のprocessID: {pid}')
    id = uuid.uuid4()
    for i in range(1):
        conversion.progress = i
        # conversion.
        sleep(1)
    conversion.output = "本日は良い天気であります"
    conversion.converted_at = datetime.datetime.now()
    conversion.is_finished = True
    conversion.save()
    # with open("./sample.txt", mode='w') as f:
    #     f.write(f"id: {id}番，処理開始します")
    #     print("変換を開始しました")
    #     sleep(5)
    #     print("変換が完了しました")
    #     f.write(f"id: {id}番，処理完了しました")
