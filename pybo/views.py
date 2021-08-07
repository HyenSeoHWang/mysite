from django.shortcuts import render
from django.http import HttpResponse # HttpResponse 는 사용자가 요청한 페이지에 응답할때 사용하는 장고의 클래스이다

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다!")
