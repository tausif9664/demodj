from django.urls import path, re_path
from workflowtest import views as workflow_views

urlpatterns = [
    path('workflowTest', workflow_views.workflowTest, name='workflowTest'),
    path('workflowTestDetails/<int:pk>/', workflow_views.workflowTestDetails_id, name='workflowTestDetails_id'),
    path('history_wf/<int:pk>/', workflow_views.history_wf, name='history_wf'),
    path('recup_wos_wf/<int:pk>/', workflow_views.recup_wos_wf, name="recup_wos_wf"),
    path('results_wf/<int:pk>/', workflow_views.results_wf, name='results_wf'),
]