from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .models import Post, DayTaskSheet, DayTask, Order, SerialNumber, ControlInput
from .forms import DayTaskForm, ControlInputForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms


# def home(request):
#     context = {
#             'posts': Post.objects.all(),
#             'orders': Order.objects.all(),
#             }
#     return render(request, 'blog/home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['orders'] = Order.objects.all()
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # ordering = ['order_num']
    # paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['controlinputs'] = ControlInput.objects.filter(serial_number__order_number__post_id=context[
            'object'].pk)
        return context

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'purchaser']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PlanView(ListView):
    model = Post
    template_name = 'blog/plan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.prefetch_related('order_set', 'order_set__serialnumber_set')
        return context


class DayTaskSheetCreateView(CreateView):
    model = DayTaskSheet
    fields = ['shop']

    def form_valid(self, form, *args, **kwargs):
        form.instance.shop_master = self.request.user
        return super().form_valid(form)


class DayTaskCreateView(CreateView):
    model = DayTask
    fields = ['site', 'worker', 'serial_number', 'operation', 'time']

    # def form_valid(self, form, *args, **kwargs):
    #     form.instance.fields['site'].queryset = self.request.site.site_set.all()
    #     return super().form_valid(form)


class DayTaskSheetDetailView(DetailView):
    model = DayTaskSheet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daytasks'] = DayTask.objects.filter(sheet__id=context['object'].pk)
        return context


class DayTaskSheetListView(ListView):
    model = DayTaskSheet
    template_name = 'blog/daytasksheet_list.html'
    context_object_name = 'daytasksheets'
    ordering = ['-date']
    paginate_by = 50


# @login_required
def daytask(request, sheet_id):
    if request.method == 'POST':
        dt_form = DayTaskForm(request.POST)
        if dt_form.is_valid():
            dt = dt_form.save(commit=False)
            dt.sheet_id = sheet_id
            dt.save()
            messages.success(request, f'Account has been updated')
            return redirect('daytasksheet-detail', sheet_id)
    else:
        dt_form = DayTaskForm(instance=request.user)
    context = {
            'dt_form': dt_form,
            }
    return render(request, 'blog/daytask_form.html', context)


def control_input(request, pk):
    if request.method == 'POST':
        ci_form = ControlInputForm(request.POST,
                                   request.FILES)
        if ci_form.is_valid():
            ci_form.save()
            messages.success(request, f'Control Input Saved')
            return redirect('post-detail', pk)
    else:
        ci_form = ControlInputForm(instance=request.user)
        ci_form.fields['serial_number'] = forms.ModelChoiceField(SerialNumber.objects.filter(order_number__post_id=pk))
    context = {
            'form': ci_form,
            }
    return render(request, 'blog/control_input_form.html', context)
