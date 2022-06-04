import requests
from celery import shared_task


@shared_task
def PDFwriter(url):
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(f'pdfs/{file_name}', mode='wb') as fd:
        fd.write(response.content)
