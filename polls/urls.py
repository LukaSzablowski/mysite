from django.urls import path

from . import views
from .views import IndexView, DetailView, ResultsView

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    # added the word 'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

