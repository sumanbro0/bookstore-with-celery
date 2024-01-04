# install requirements.txt
    $ pip install -r requirements.txt

# run server
    $ py manage.py runserver

# run celery worker for scheduled task

    - for windows

    $ celery -A task9 worker -l info -P solo

    - for linux

    $ celery -A task9 worker -l info


# run celery beat

    $ celery -A task9 beat --loglevel=info


this will create a new notification everyminute . check celery.py for more customization in corntab(hours=,minutes=,.......)