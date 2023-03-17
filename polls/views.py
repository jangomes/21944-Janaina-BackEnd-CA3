from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from django.http import QueryDict
from django.db.models import Q
import polls.models

from .models import Choice, Question

# Here I will validate user input and prevent SQL injection by using Django's QueryDict and django.db.models classes
# I used Django's QueryDict class to parse the request's query parameters, and validate them before passing them to the database query.
# I also use Django's Q objects to construct the WHERE clause of the SQL query in a way that prevents SQL injection attacks.
def my_view(request):
    query_params = request.GET or request.POST
    query_dict = QueryDict(query_params)

    # Perform input validation on the query parameters
    param1 = query_dict.get('param1')
    param2 = query_dict.get('param2')

    if not param1 or not param2:
        return HttpResponseBadRequest('Missing query parameters')

    # Prevent SQL injection using Django's Q objects
    my_model_objects = MyModel.objects.filter(Q(param1=param1) & Q(param2=param2))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

