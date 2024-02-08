from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, View
from webapp.models import Comment, Publication

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
