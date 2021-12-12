from django.urls import path

from logisticapp.views import LogisticExpenseHeaderCreate,AuditData, RequestLogs 




urlpatterns = [
    path('logisticexpcreate', LogisticExpenseHeaderCreate.as_view()),
    path('auditdata', AuditData.as_view()),
    path('requestlog', RequestLogs.as_view()),


    # path('<int:id>', ContactDetailView.as_view())

]
