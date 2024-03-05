from django.urls import path, re_path
from users import views as user_views

urlpatterns = [
    path('history/<int:pk>/',user_views.history, name='history'),
    path('loadTest/', user_views.loadTest, name='loadTest'),
    path('results/<int:pk>/',user_views.results, name='results'),
    path('pagelinks/<int:pk>/',user_views.loadTestDetails_id, name='loadTestDetails_id'),
    path('recup_wos/<int:pk>/',user_views.recup_wos,name="recup_wos"),
    path('results/', user_views.search,name="search"),
    path('clearsorting/', user_views.sort,name="sort"),
    path('Export/',user_views.Export,name="Export"),
]