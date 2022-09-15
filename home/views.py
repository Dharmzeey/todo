from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .models import Todo

class HomeView(LoginRequiredMixin, View):
  template_name = 'home/index.html'
  
  def get(self, request):
    obj = Todo.objects.filter(owner=request.user)
    ctx = {
      'todos': obj
    }
    return render(request, self.template_name, ctx)

home = HomeView.as_view()

class CreateTodo(LoginRequiredMixin, CreateView):
  model = Todo
  fields = ["title", "description", "completed"]
  success_url = reverse_lazy("home")
  
  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super(CreateTodo, self).form_valid(form)
create_todo = CreateTodo.as_view()

class ReadTodo(LoginRequiredMixin, DetailView):
  model = Todo
read_todo = ReadTodo.as_view()

class UpdateTodo(LoginRequiredMixin, UpdateView):
  model = Todo
  fields = ["title", "description", "completed"]
  def get_success_url(self):
    pk = self.kwargs['pk']
    return reverse_lazy('todo_read', kwargs={'pk': pk})
update_todo = UpdateTodo.as_view()

class DeleteTodo(LoginRequiredMixin, DeleteView):
  model = Todo
delete_todo = DeleteTodo.as_view()
