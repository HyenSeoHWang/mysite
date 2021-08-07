from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),#config.urls 에서 받은 호출 이후 veiws.index 호출 
    #path 함수의 인자가 ''인 이유는 이미 config.urls에서 매핑을 받았기때문이다. 그러니까 최종적으로 호출된 URL은
    # pybo/ /이다.pybo.urls 에서는 ''을 매핑한것이기 때문이다. 만약 ''가 아닌 'create'을 코딩한다면 최종 URL은 /pybo/create/가 되는것!
]