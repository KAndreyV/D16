from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, )
from .models import Advertisement, Response, User
from .filters import AdvertisementFilter
from .forms import AdvertisementForm, ResponseForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class AdvertisementsList(ListView):
    model = Advertisement
    ordering = '-time_in'
    template_name = 'advertisements.html'
    context_object_name = 'advertisements'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdvertisementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AdvertisementDetail(DetailView):
    model = Advertisement
    template_name = 'advertisement.html'
    context_object_name = 'advertisement'


class AdvertisementCreate(LoginRequiredMixin, CreateView):
    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'advertisement_create.html'

    #создание объявления с автосохранением автора для объявления
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        form = AdvertisementForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                new_advertisement = form.save(commit=False)
                new_advertisement.author = request.user
                new_advertisement.save()
                return redirect('/advertisements/')
        return render(request, 'advertisement_create.html', locals())


class AdvertisementUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('board_app.change_advertisement',)
    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'advertisement_edit.html'
    context_object_name = 'advertisement'


class AdvertisementDelete(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement_delete.html'
    context_object_name = 'advertisement'
    success_url = reverse_lazy('advertisement_list')


class AuthorAdvertisementsList(ListView):
    model = Advertisement
    ordering = '-time_in'
    template_name = 'advertisements_of_author.html'
    context_object_name = 'authoradvertisement'
    paginate_by = 10

    def get_queryset(self):
        self.author = get_object_or_404(User, id=self.kwargs['pk'])
        queryset = Advertisement.objects.filter(author=self.author)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context


class ResponseCreate(PermissionRequiredMixin, CreateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_edit.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        form = ResponseForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                new_response = form.save(commit=False)
                new_response.advertisement_id = self.kwargs.get('pk')
                new_response.commentator = request.user
                new_response.save()
                return redirect(f'/advertisements/{new_response.advertisement_id}')
        return render(request, 'response_edit.html', locals())


class ResponseList(ListView):
    model = Response
    ordering = '-time_create'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 10


class ResponseDetail(DetailView):
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'


@login_required
def confirm(self, *args, **kwargs):
    Response.objects.filter(id=get.id).update(status=True)
    return redirect('/advertisements/responses/')


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'response_delete.html'
    context_object_name = 'response'
    success_url = reverse_lazy('response_list')
