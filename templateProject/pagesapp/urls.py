from django.urls import path
from.views import HomePageView, AboutPageView,NewsPageView,CompanyPageView,CreaterPageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('/about',AboutPageView.as_view(),name='about'),
    path('/news',NewsPageView.as_view(),name='news'),
    path('/company',CompanyPageView.as_view(),name='companies'),
    path('/creater',CreaterPageView.as_view(),name='creater'),
]