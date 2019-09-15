"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.comment import (
    DeleteComment , CommentCreateView, CommentDetailView, CommentListView, CommentUpdateView)


urlpatterns = [
    path('comments', CommentListView.as_view(), name='comments'),
    path('comment/add/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/update', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', DeleteComment, name='comment-delete'),
]