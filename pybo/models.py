'''
*장고에서 사용하는 속성(Field)타입들 
https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

* models.py는 데이터베이스를 처리하기 위한 파일이다.
* SQL쿼리문을 이용해야하지만 장고를 통해 SQL문을 작성하지 않아도 가능하다.
* 데이터베이스 모델을 작성할때에는 데이터베이스 모델의 속성을 잘 파악해야한다.
* 데이터베이스에서 데이터를 저장하기 위한 데이터 집합의 모임을 '테이블'이라한다
* 테이블을 생성하기위해서는 pybo 라는 앱을 setting.py에 등록해야한다
* 파이썬 shell에서 데이터를 조회하는 방법이 담긴 URL : https://docs.djangoproject.com/en/3.0/topics/db/queries/
'''

from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)#CharFiled =>글자수제한이 있는 텍스트
    content = models.TextField()#TextFeild =>글자수 제한이 없는 텍스트
    create_date = models.DateField()#DateFeild =>날짜와 시간에 관계된 속성이 필요할때

    def __str__(self): #파이썬 shell에서 등록된 질문을 조회할때 id(=pk)가 아닌 subject내용으로 나오게하는 함수
        return self.subject

class Answer(models.Model):#Anser 모델은 질문에 대한 답이기 때문에 Question모델의 속성을 가져와야한다
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#ForeignKey => 기존모델의 속성으로 연결할때
    # on_delete=models.CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미이다.
    content = models.TextField()
    create_date = models.DateTimeField()
