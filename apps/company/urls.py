from django.conf.urls import url
from apps.company.views import CompanyIndex

urlpatterns = [
    url(r'^$', CompanyIndex.as_view()),
]