from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse

from .models import *


class ObjectDetailMixin:
    model = None
    template = None
    is_editable = True

    def get(self, request, id=None, slug=None):
        if slug:
            obj = get_object_or_404(self.model, slug__iexact=slug)
        else:
            obj = get_object_or_404(self.model, id=id)
        return render(request, self.template, context={
            self.model.__name__.lower(): obj,
            'is_editable': self.is_editable,
            'admin_object': obj,
        })


class ObjectsListMixin:
    model = None
    template = None
    objects_on_page = None

    def get(self, request):
        search_par = request.GET.get('search', None)
        print(search_par)

        if search_par:
            objects = self.model.objects.filter(
                Q(title__icontains=search_par) | Q(description__icontains=search_par)
            )
        else:
            objects = self.model.get_sorted_query()

        page_number = request.GET.get('page', 1)
        paginator = Paginator(objects, self.objects_on_page)
        page = paginator.get_page(page_number)

        context_name = '{}{}'.format(self.model.__name__.lower(), '_page')
        return render(request, self.template, context={
            context_name: page,
            # context_name: objects,
        })


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    form_model = None
    model = None
    template = None

    def get(self, request, slug=None, id=None):
        if slug:
            obj = get_object_or_404(self.model, slug__iexact=slug)
        else:
            obj = get_object_or_404(self.model, id=id)

        bound_form = self.form_model(instance=obj)
        return render(request, self.template, context={
            'form': bound_form,
            self.model.__name__.lower(): obj
        })

    def post(self, request, slug=None, id=None):
        if slug:
            obj = get_object_or_404(self.model, slug__iexact=slug)
        else:
            obj = get_object_or_404(self.model, id=id)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            updated_object = bound_form.save()
            return redirect(updated_object)
        else:
            return render(request, self.template, context={
                'form': bound_form,
                self.model.__name__.lower(): obj
            })


class ObjectDeleteMixin:
    model = None
    template = None

    def get(self, request, id=None, slug=None):
        if slug:
            obj = get_object_or_404(self.model, slug=slug)
        else:
            obj = get_object_or_404(self.model, id=id)

        return render(request, self.template, context={
            'obj': obj
        })

    def post(self, request, id=None, slug=None):
        if slug:
            obj = get_object_or_404(self.model, slug=slug)
        else:
            obj = get_object_or_404(self.model, id=id)

        objects_list_url = obj.get_list_url()
        obj.delete()

        return redirect(objects_list_url)
