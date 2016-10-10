from django.conf.urls import include, url

from .views import BlockValidateView, BlockDisplayView, BlockUpdateView

block_patterns = [
    url(r'^validate/$', BlockValidateView.as_view(), name='list'),
    url(r'^create/(?P<type>\d\w+)$', BlockDisplayView.as_view(), name='create'),
    url(r'^id/(?P<id>\d+)$', BlockUpdateView.as_view(), name='update'),
]
