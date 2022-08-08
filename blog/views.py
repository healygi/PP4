from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status = 1)
        post = get_object_or_404(queryset, slug = slug)
        comments = post.comments.filter(approved = True).order_by("-created_on")
        liked = False
        if post.likes.filter(id = self.request.user.id).exists():
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
                "comment_form": CommentForm()
                #"comments_count": comments,
                #"count": count
            },
         )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status = 1)
        post = get_object_or_404(queryset, slug = slug)
        comments = post.comments.filter(approved = True).order_by("-created_on")
        liked = False
        if post.likes.filter(id = self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit = False)
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

class PostLike(View):


    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug = slug)
        if post.likes.filter(id = request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# EDIT COMMENTS

class PostCommentEdit(UpdateView):
    model = Comment
    fields = ['post']

    success_url ="/"
    # template_name_suffix = '_update_form'

    # def edit_comment(self, request, slug, *args, **kwargs):
    #     post = get_object_or_404(Post, slug=slug)
    #     user = get_object_or_404(Comment, user=request.user, slug=slug)

    #     if request.method == "POST":
    #         comment_form = CommentForm(request.POST, instance=user)
    #         if comment_form.is_valid():
    #             comment_form.save()
    #             messages.success(request, f'We have updated your review for {post.name}.')

    #             return HttpResponseRedirect(reverse('post_detail', args=[self.post.slug]))

    #         else:
    #              messages.error(request, f'Sorry we were unable to update your request')

    #     else:
    #         comment_form = CommentForm(instance=user)

    #     return render(
    #         request,
    #         "post_detail.html",
    #          {
    #             "post": post,
    #             "comment_form": comment_form,
    #         },
    #      ) 

# DELETE COMMENTS

class PostCommentDelete(View):
    model = Comment
    fields = ['body']

    def delete_comment(self, request, slug, *args, **kwargs):
        comment = get_object_or_404(Comment, slug=slug)
        r = request.user
        if ( 
            comment.name == r.username and r.is_authenticated
        ):
            comment.delete()
            # request.user.name == comment.user.name:
            # Comment.objects.get(slug = slug).delete()

        message.success(request, 'Your comment has been deleted.')
        return HttpResponseRedirect(reverse('post_detail', args=[self.post.slug])) 