
from django.urls import path, include
from webscraper.views import scraper, about, download_pdf


urlpatterns = [
    path('', scraper.WebScraperView.as_view()),
    path('about/', about.AboutView.as_view(), name='about'),
    path('download-pdf/', download_pdf.DownloadPDF.as_view(), name='download-pdf'),
]
