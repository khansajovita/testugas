from django.urls import path
from mywatchlist.views import show_html
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_html, name='show_html'),
    path('html', show_html, name='show_html'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
]