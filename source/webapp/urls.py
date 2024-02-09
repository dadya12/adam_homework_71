from django.urls import path
from webapp.views.publication_views import HomeView, PublicationCreateView, PublicationLikeView, LikePubUser
from webapp.views.comments_views import CommentView, LikeCommentUser, CommentCreateView

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('publications/create/', PublicationCreateView.as_view(), name='publication_create'),
    path('publications/like/<int:pk>/', PublicationLikeView.as_view(), name='publication_like'),
    path('comments/<int:pk>', CommentView.as_view(), name='comments'),
    path('publications/<int:pk>/like/', LikePubUser.as_view(), name='user_likes'),
    path('comments/<int:pk>/like/', LikeCommentUser.as_view(), name='comment_likes'),
    path('comments/<int:pk>/create/', CommentCreateView.as_view(), name='comment_create')

]
