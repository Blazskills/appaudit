from django.urls import path

from logisticapp.views import LogisticExpenseHeaderCreate 




urlpatterns = [
    path('logisticexpcreate', LogisticExpenseHeaderCreate.as_view()),
    # path('<int:id>', ContactDetailView.as_view())

]
