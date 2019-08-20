from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
)
from django.views.generic.detail import BaseDetailView
from main import models,forms
# Create your views here.

class Index(ListView):
    model = models.Question
    template_name = 'main\index.html'

class question(BaseDetailView , FormView):
    model = models.Question
    template_name = 'main\question.html'
    form_class = forms.AnswerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['answer'] = models.Answer.objects.get(
        question = self.get_object(),
        user = self.request.user
        )
        return data

    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.question = self.get_object()
        obj.save()
        return HttpResponseRedirect('/')