from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def index(request):
    '''
    pybo 질문 목록 출력
    '''
    #Question(models에 존재하는 클래스)의 objects(객체)를 생성날짜의 역순(최신순)으로 정렬해라
    question_list = Question.objects.order_by('-create_date')#order_by는 조회결과를 정렬하는 함수, -create_date 생성날짜를 역순으로 정렬
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)#즉,위에서 사용한 render 함수는 question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML을 리턴한다.
    #render함수의 context 인수는 템플릿에 표시 할 변수를 제공한다. 즉, 여기서는 question_list.html에서 사용할 question_list를 엑세스했음

def detail(request, question_id):
    '''
    pybo 질문 내용 출력
    '''
    question = get_object_or_404(Question, pk =question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)  

def question_create(request):
    '''
    pybo 질문등록
    '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)