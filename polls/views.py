from pprint import pprint

# Create your views here.
from django.template import loader

from django.views import generic
from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""Generic View 사용하지 않은 코드"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
#from polls.models import Question, Choice
#def index(request):
#    print("pprint(dir(request))")
#    pprint(dir(request))
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list': latest_question_list
#    }
#
#    #pprint(dir(latest_question_list[0]))
#    '''
#    # 주석된 코드와 아래 코드는 동일한 기능을 수행함
#    template = loader.get_template('polls/index.html')
#    return HttpResponse(template.render(context, request))
#    '''
#    return render(request, 'polls/index.html',context)
#
#
#def detail(request, question_id):
#
#    """
#    # 주석된 코드와 아래 코드는 동일한 기능을 수행함
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    """
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question' : question})
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

