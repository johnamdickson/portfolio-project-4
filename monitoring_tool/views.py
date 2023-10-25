from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Emission, EmissionCheck


class EmissionHome(generic.ListView):
    model = Emission
    queryset = Emission.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 20


class EmissionList(generic.ListView):
    model = Emission
    queryset = Emission.objects.order_by("-created_on")
    template_name = "emission.html"
    paginate_by = 20


class Emissions(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Emission.objects
        emission = get_object_or_404(queryset, slug=slug)
        title = emission.title
        description = emission.description
        image_url = emission.emission_image.url
        location = emission.location

        return render(
            request,
            'emission_detail.html',
            {
                "title": title,
                "description": description,
                "image_url": image_url,
                "location": location
            },
        )
    
    # def post(self, request, *args, **kwargs):

    #     queryset = Emission.objects.filter(status=0)
    #     post = get_object_or_404(queryset, slug=slug)
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment_form.instance.email = request.user.email
    #         comment_form.instance.name = request.user.username
    #         comment = comment_form.save(commit=False)
    #         comment.post = post
    #         comment.save()
    #     else:
    #         comment_form = CommentForm()

    #     return render(
    #         request,
    #         "emission.html",
    #         {
    #             "emission": post,
    #             "comments": comments,
    #             "commented": True,
    #             "comment_form": comment_form,
    #             "liked": liked
    #         },
    #     )


class EmissionChecks(generic.ListView):
    model = EmissionCheck
    queryset = EmissionCheck.objects.filter(status=0).order_by("-date_checked")
    template_name = "emission_checks.html"
    paginate_by = 6
