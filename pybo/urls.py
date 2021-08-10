from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('',views.index , name = 'index'),#config.urls 에서 받은 호출 이후 veiws.index 호출한다
    #path 함수의 인자가 ''인 이유는 이미 config.urls에서 매핑을 받았기때문이다. 그러니까 최종적으로 호출된 URL은
    #pybo/ /이다.pybo.urls 에서는 ''을 매핑한것이기 때문이다. 만약 ''가 아닌 'create'을 코딩한다면 최종 URL은 /pybo/create/가 되는것이다
    #3번째 인수 : http://localhost:8000/pybo/라는 URL에는 'index'라는 이름을 부여했다

    path('<int:question_id>/', views.detail, name = 'detail'),

    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

    path('question/create/', views.question_create, name='question_create'),
]