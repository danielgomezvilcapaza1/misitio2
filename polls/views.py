from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from polls.models import Poll, Choice
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

class IndexView (generic.ListView):
    #latest_poll_list = Poll.objects.order_by('pub_date')[:5]
    template_name = 'polls/index.html'
    Context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """ devuelve las ultimas 5 encuestas publicadas."""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
  
class ResultsView (generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
  
def vote (request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html',{
            'poll':p,
            'error_message':"usted no ha seleccionado una opcion.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id)))

