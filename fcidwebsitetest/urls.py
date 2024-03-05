from django.urls import path, re_path
from fcidwebsitetest import views as fcidwebsitetest_views

urlpatterns = [
path('fcidwebsitetest/',fcidwebsitetest_views.fcidwebsitetest, name='fcidwebsitetest'),
    path('fcidwebsitetestDetails/<int:pk>/', fcidwebsitetest_views.fcidwebsitetestDetails_id, name='fcidwebsitetestDetails_id'),
    path('history_FT/<int:pk>/',fcidwebsitetest_views.history_FT, name='history_FT'),
    path('recup_wos_FT/<int:pk>/',fcidwebsitetest_views.recup_wos_FT,name="recup_wos_FT"),
    path('results_FT/<int:pk>/',fcidwebsitetest_views.results_FT, name='results_FT'),
]