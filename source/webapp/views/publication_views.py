from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.models import Publication, Comment
from webapp.forms import PublisherForm

class LikePubUser(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        public = get_object_or_404(Publication, pk=pk)
        if request.user in public.users_likes.all():
            public.users_likes.remove(request.user)
        else:
            public.users_likes.add(request.user)
        return JsonResponse({'count': public.users_likes.count()}, safe=False)

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'publications'

    def get_queryset(self):
        return Publication.objects.filter(author__in=self.request.user.subscriptions_users.all()).order_by('-created')


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'publication/publication_create.html'
    form_class = PublisherForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class PublicationLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        publication = get_object_or_404(Publication, pk=pk)
        if request.user in publication.users_like.all():
            publication.users_like.remove(request.user)
        else:
            publication.users_like.add(request.user)

        publication.likes_count = publication.users_like.count()
        publication.save()
        return redirect('webapp:index')

