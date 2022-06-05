import csv
import os
import requests
from celery import shared_task
from celery_progress.backend import ProgressRecorder
from webscraper.models import PDFLink

@shared_task(bind=True)
def PDFwriter(self, url):
    progress_recorder = ProgressRecorder(self)
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(f'pdfs/{file_name}', mode='wb') as fd:
        fd.write(response.content)
    progress_recorder.set_progress(1, 2)


@shared_task
def CSVwriter(data):
    with open('pdf_urls.csv', mode='w', encoding='UTF-8') as fd:
        writer = csv.writer(fd)
        writer.writerow(data)


def CSVreader(path):
    if os.path.exists(path):
        with open(path, mode='r') as fd:
            url_reader = csv.reader(fd, delimiter=',')
            return list(url_reader)
    else:
        return []


@shared_task
def InsertDBData(data):
    for url in data:
        try:
            PDFLink.objects.create(url=url)
        except IntegrityError as e:
            print(e)
            return False


def celery_worker_status():
    ERROR_KEY = "ERROR"
    try:
        from celery.task.control import inspect
        insp = inspect()
        d = insp.stats()
        if not d:
            d = {ERROR_KEY: 'No running Celery workers were found.', is_running: False}
        else:
            d = {ERROR_KEY: 'No running Celery workers were found.', is_running: True}
    except IOError as e:
        from errno import errorcode
        msg = "Error connecting to the backend: " + str(e)
        if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
            msg += ' Check that the RabbitMQ server is running.'
        d = {ERROR_KEY: msg}
    except ImportError as e:
        d = {ERROR_KEY: str(e)}
    return d
