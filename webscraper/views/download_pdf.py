import os
from celery import group
from django.views import View
from django.shortcuts import render
from webscraper.utils import CSVreader, PDFwriter, celery_worker_status
from webscraper.models import PDFLink


class DownloadPDF(View):
    def get(self, request):

        pdf_url_qs = PDFLink.objects.all()
        pdf_url_count = PDFLink.objects.all().count()

        if pdf_url_count == 0:
            return render(request, 'error.html',
                          context={'message': "You have not scrape the PDF URLs"})

        if celery_worker_status().get('is_running', None):
            return render(request, 'scrape.html')

        result = group(PDFwriter.s(pdf_url.url)
                       for pdf_url in pdf_url_qs)()
        return render(request, 'scrape.html', context={'task_ids': [task for parents in result.children for task in parents.as_list()[::-1]]})
