import datetime

from django.db import models
from django.utils import timezone

'''
- 장고의 모델은 [models.Model]을 상속받아서 생성하며, 이 클래스가 데이터베이스와 ORM을 이용해 동작하는 기능을 가짐
- Choice 모델이 Foreign Key로 Question 모델을 가진다는 것은 Choice 모델이 Question에 소속된다는 것을 의미
- __str__ 메서드는 관리자 화면이나 쉘에서 객체를 출력할 때 표시할 내용
'''

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 관리자 화면 목록 커스터마이징
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

