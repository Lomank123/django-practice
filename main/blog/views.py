from blog.forms import BlogCommentModelForm
from blog.models import BlogComment, BlogPost
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView


class BlogPostDetailView(FormView):
    form_class = BlogCommentModelForm
    template_name = 'blog/blog-detail.html'

    def get_success_url(self):
        return f'/blog/{self.kwargs["pk"]}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(BlogPost.objects.select_related("author").all(), pk=self.kwargs["pk"])
        context["post"] = post
        context["comments"] = BlogComment.objects.filter(post_id=post.id).select_related("user", "post")
        # Sessions example: number of times you have visited this page during the session
        context["num_visits"] = self.request.session.get('num_visits', 0)
        return context

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.post_id = self.kwargs["pk"]
        response = super().form_valid(form)
        form.save()
        return response

    def get(self, request, pk):
        # Increment each time user visits this page
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return super().get(request)
