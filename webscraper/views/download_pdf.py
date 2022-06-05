import os
from celery import group
from django.views import View
from django.shortcuts import render
from webscraper.utils import CSVreader, PDFwriter, celery_worker_status
from webscraper.models import PDFLink


class DownloadPDF(View):

    # pdf_urls = CSVreader("pdf_urls.csv")

    # print(pdf_url_qs)
    # Get pdf urls into memory
    # validate url exist
    # check if it's not currently running

    def get(self, request):

        pdf_url_qs = PDFLink.objects.all()
        pdf_url_count = PDFLink.objects.all().count()
        is_running = False

        if pdf_url_count == 0:
            return render(request, 'error.html',
                          context={'message': "You have not scrape the PDF URLs"})
        # if is_running:
        #     return render(request, 'scrape.html')

        if celery_worker_status().get('is_running', None):
            print("IS CURRENTLY RUNNING")
            print("Got here")
            return render(request, 'scrape.html')

        # start downloading the webpage
        # total_pdfs = len(self.pdf_urls)
        result = group(PDFwriter.s(pdf_url.url)
                       for pdf_url in pdf_url_qs)()
        # is_running = not result.successful()
        # if os.path.exists("pdf_urls.csv"):
        #     os.remove("pdf_urls.csv")
        return render(request, 'scrape.html', context={'task_ids': [task for parents in result.children for task in parents.as_list()[::-1]]})
