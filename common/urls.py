from django.urls import path

from common.views import home_page_view, contact_page_view, ContactPageView

app_name = 'common'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]