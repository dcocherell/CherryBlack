web: gunicorn CherryBlack.wsgi

worker: celery -A CherryBlack worker --loglevel=info
beat: celery -A CherryBlack beat --loglevel=info