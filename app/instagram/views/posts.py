from django.views.generic import ListView

from instagram.models import Posts


class PostsListView(ListView):
    template_name = 'posts_list.html'
    model = Posts
    context_object_name = 'posts'
    ordering = ('created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = self.request.user
        context['posts'] = Posts.objects.all()
        return context
