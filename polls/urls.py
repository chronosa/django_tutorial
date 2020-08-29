from django.urls import path
from . import views

'''
* path(route, view, kwargs, name)
  - kwargs : view에 전달할 값들
  - name : route의 이름을 의미. 이 이름을 가지고 원하는 곳에서 주소를 호출해 출력하거나 사용 가능
※ config/urls.py에서 polls.urls를 연결해주어야 함

* 각 URL에 있는 <>(화살괄호)는 변수를 의미함. 이 부분에 해당하는 값을 뷰에 인자로 전달
'''
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]

# URL Namespace 설정 - 각각의 뷰가 어느 앱에 속한 것인지 구분하도록 한다.
app_name = 'polls'
