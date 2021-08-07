"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#url.py는 브라우저가 페이지요청을 받았을때 가장 먼저 호출되는 파일이다.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),#pybo/ 라는 url이 요청되면, include('pybo.urls')를 호출하라는 내용이다. 
    #이곳은 최종url이기 때문에 pybo라는 앱의 urls을 불러오기 위해 include 기능을 사용한것이다. =>즉, pybo/를 요청 받으면 pybo.urls로 매핑!

]