from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Blog, Topic, Tag
from .utils import ObjectDetailMixin, ObjectsListMixin, ObjectCreateMixin
from .utils import ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, MLGForm, TopicForm


def test(request):
    print(request.user)
    # fill_texts(Blog)
    return HttpResponse('')


class BlogsList(ObjectsListMixin, View):
    model = Blog
    template = 'blog_engine/blogs_list.html'
    objects_on_page = 3


class BlogDetail(ObjectDetailMixin, View):
    model = Blog
    template = 'blog_engine/blog_detail.html'
    is_editable = False


class TopicDetail(ObjectDetailMixin, View):
    model = Topic
    template = 'blog_engine/topic_detail.html'


class TopicCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TopicForm
    template = 'blog_engine/topic_create.html'
    raise_exception = True


class TopicUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    form_model = TopicForm
    model = Topic
    template = 'blog_engine/topic_update_form.html'
    raise_exception = True


class TopicDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Topic
    template = 'blog_engine/topic_delete_form.html'
    raise_exception = True
    # objects_list_url = 'topics_'


class TagsList(ObjectsListMixin, View):
    model = Tag
    template = 'blog_engine/tags_list.html'
    objects_on_page = 3


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog_engine/tag_create.html'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog_engine/tag_detail.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    form_model = TagForm
    model = Tag
    template = 'blog_engine/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog_engine/tag_delete_form.html'
    raise_exception = True


class MyForm(View):

    def get(self, request):
        form = MLGForm()
        return render(request, 'blog_engine/test_template.html', context={'form': form})

    def post(self, request):
        # print(request.POST)
        bound_form = MLGForm(request.POST)
        if bound_form.is_valid():
            message = 'ok'
        else:
            message = 'not ok'
        return HttpResponse(message)
