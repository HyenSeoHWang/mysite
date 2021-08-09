from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse # HttpResponse 는 사용자가 요청한 페이지에 응답할때 사용하는 장고의 클래스이다
from .models import Question, Answer
from django.utils import timezone

def index(request):
    '''
    pybo 목록 출력
    '''
    #Question(models에 존재하는 클래스)의 objects(객체)를 생성날짜의 역순(최신순)으로 정렬해라
    question_list = Question.objects.order_by('-create_date')#order_by는 조회결과를 정렬하는 함수, -create_date 생성날짜를 역순으로 정렬
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)#즉,위에서 사용한 render 함수는 question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML을 리턴한다.
    #render함수의 context 인수는 템플릿에 표시 할 변수를 제공한다. 즉, 여기서는 question_list.html에서 사용할 question_list를 엑세스했음

def detail(request, question_id):
    question = get_object_or_404(Question, pk =question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    answer = Answer(question=question, content= request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id) #redirect를 사용한 이유는 답변생성화면을 작성 후 다시 답변생성화면을 유지하기위함
    #redirect는 url로 이동하고 render는 템플릿을 불러온다. 즉,여기서는 detail URL로 이동해서 다시 views로 넘어간다