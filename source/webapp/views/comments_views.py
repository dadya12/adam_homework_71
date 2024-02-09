from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView
from webapp.models import Comment, Publication
from webapp.forms import CommentForm

class LikeCommentUser(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return JsonResponse({'count': comment.likes.count()}, safe=False)

class CommentView(DetailView):
    model = Comment
    template_name = 'comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(pk=self.object.pk)
        context['comments'] = Comment.objects.filter(post_id=self.object.pk)
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comments/comment_create.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        publication = get_object_or_404(Publication, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.post = publication
        comment.author = self.request.user
        comment.save()
        return redirect('webapp:index')
