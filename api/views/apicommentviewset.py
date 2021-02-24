from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Comment, Review
from ..serializers.commentserializer import CommentSerializer
from ..review_permission import IsModeratorOrAdminOrAuthorOrReadOnly


class APICommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsModeratorOrAdminOrAuthorOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsModeratorOrAdminOrAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        review = get_object_or_404(Review, 
                                   pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review,
                                   pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
