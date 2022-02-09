## Django の view で非同期処理的なことがしたかった

special special thanks: https://dot-blog.jp/news/django-async-celery-redis-mac/

ターミナル 1 つ目

```bash
python manage.py runserver 0:8000
```

ターミナル 2 つ目

```bash
redis-server
```

ターミナル 3 つ目

```bash
DJANGO_SETTINGS_MODULE=config.settings celery -A config beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile /tmp/celerybeat.pid
```
