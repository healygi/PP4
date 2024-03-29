from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import redirect


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# Detail of post including comments, comment-form and likes - render page
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        count = 0

        for comments_count in comments:
            # increment
            count += 1

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "comments_count": comments,
                "count": count
            },
         )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
             },
         )

# logic for post like functionality


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# DELETE COMMENTS


class PostCommentDelete(View):

    def get(self, request, pk, *args, **kwargs):

        comment = get_object_or_404(Comment, pk=pk)
        context = {
            'comment': comment,
        }

        return render(
            request,
            'user_comments/delete-comment.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):

        comment = get_object_or_404(Comment, pk=pk)
        post = comment.post
        comment.delete()

        return redirect('post_detail', slug=post.slug)

# Edit Comments


class PostCommentEdit(View):

    def get(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        comment_form = CommentForm(data=request.POST)
        post = comment.post

        context = {
            'comment': comment,
            'comment_form': comment_form,
        }

        return render(
            request,
            'user_comments/edit-comment.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):

        comment = get_object_or_404(Comment, pk=pk)
        post = comment.post

        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            form.save()

        return redirect('post_detail', slug=post.slug)
