from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Support, Respond
from .forms import RespondForm, SupportForm


class SupportList(generic.ListView):
    queryset = Support.objects.all().filter(status=1)
    template_name = "support/index.html"
    paginate_by = 10


def support_detail(request, slug):
    """
    Display an individual :model:`support.Support`.

    **Context**

    ``support``
        An instance of :model:`support.Support`.

    **Template:**

    :template:`support/support_detail.html`
    """

    queryset = Support.objects.filter(status=1)
    supportPage = get_object_or_404(queryset, slug=slug)
    replies = supportPage.replies.all().order_by("-created_on")
    reply_count = supportPage.replies.filter(approved=True).count()

    if request.method == "POST":
        reply_form = RespondForm(data=request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.parent = request.user
            reply.support = supportPage
            reply.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    reply_form = RespondForm()

    return render(
        request,
        "support/support_detail.html",
        {
            "support": supportPage,
            "replies": replies,
            "reply_count": reply_count,
            "reply_form": reply_form,
        }
    )


def reply_edit(request, slug, reply_id):
    """
    view to edit replies to support posts
    """
    if request.method == "POST":

        queryset = Support.objects.filter(status=1)
        supportPage = get_object_or_404(queryset, slug=slug)
        replies = get_object_or_404(Respond, pk=reply_id)
        reply_form = RespondForm(data=request.POST, instance=replies)

        if reply_form.is_valid() and replies.parent == request.user:
            reply = reply_form.save(commit=False)
            reply.supportPage = supportPage
            reply.approved = False
            reply.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your reply has been updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                'hmm.. We seem to be unable to update your reply. '
                'Please try again.')

    return HttpResponseRedirect(reverse('support_detail', args=[slug]))


def reply_delete(request, slug, reply_id):
    """
    view to delete a reply
    """
    queryset = Support.objects.filter(status=1)
    supportPage = get_object_or_404(queryset, slug=slug)
    replies = get_object_or_404(Respond, pk=reply_id)

    if replies.parent == request.user:
        replies.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Your reply has been deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own replies!')

    return HttpResponseRedirect(reverse('support_detail', args=[slug]))


def support_post(request):
    """
    Display the page where a user can create a Support post
    :model:`support.Support`.

    **Context**

    ``support``
        An instance of :model:`support.Support`.

    **Template:**

    :template:`support/support_post.html`
    """

    if request.method == "POST":
        support_form = SupportForm(data=request.POST)
        if support_form.is_valid():
            userpost = support_form.save(commit=False)
            userpost.parent = request.user
            userpost.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your Support post has been submitted and is awaiting approval'
            )

    support_form = SupportForm()

    return render(
        request,
        'support/support_post.html',
        {
            "support_form": support_form
        })
