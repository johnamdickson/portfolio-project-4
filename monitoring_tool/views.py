from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Emission, EmissionCheck
from .forms import EmissionSubmissionForm, EmissionCloseOutForm
from datetime import datetime


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
                "location": location,
                "slug": slug,
            },
        )

    def close(request, slug, *args, **kwargs):
        queryset = Emission.objects
        emission = get_object_or_404(queryset, slug=slug)
        form = EmissionCloseOutForm()
        if request.user.has_perm('monitoring_tool.change_emission'):
            if request.method == 'POST':
                # check if user has permissions to add emissions ie emission admin.
                # issue uploading image to DB from html form.
                # Solution from Stack Overflow:
                # https://stackoverflow.com/questions/45912825/image-upload-field-works-in-django-admin-but-not-working-in-template
                form = EmissionCloseOutForm(request.POST, instance=emission)
                if form.is_valid():
                    form.instance.closed_by = f'{User.objects.get(username=request.user)}'
                    form.instance.status = 1
                    form.instance.close_out_date = datetime.now()
                    form.save()
                    messages.success(
                        request,
                        f" {form.instance.title} has been successfully closed."
                        )
                    return HttpResponseRedirect(reverse('emissions'))
                else:
                    error = []
                    for field in form:
                        if field is not None:
                            error += field.errors
                    messages.error(request, error)
        else:
            messages.warning(
                request,
                f"You do not have the necessary permissions "
                "to close an emission.\n Please contact your"
                " system administrator.")
            return HttpResponseRedirect(reverse('emissions'))

        context = {'form': form}
        return render(request, 'close-emission.html', context)


class EmissionChecks(generic.ListView):
    model = EmissionCheck
    queryset = EmissionCheck.objects.filter(status=0).order_by("-date_checked")
    template_name = "emission_checks.html"
    paginate_by = 6


def addEmission(request):
    form = EmissionSubmissionForm()
    # check if user has permissions to add emissions ie emission admin.
    # issue uploading image to DB from html form.
    # Solution from Stack Overflow:
    # https://stackoverflow.com/questions/45912825/image-upload-field-works-in-django-admin-but-not-working-in-template
    if request.user.has_perm('monitoring_tool.add_emission'):
        if request.method == 'POST':
            form = EmissionSubmissionForm(request.POST, request.FILES)
            # access form image name from request.FILES and use conditional code to proceed
            # or generate error message.
            form_images = request.FILES.getlist('emission_image', None)
            form_image = form_images[0]
            if str(form_image).endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp')):
                if form.is_valid():
                    form.instance.username = User.objects.get(
                                        username=request.user)
                    form.instance.status = 0
                    form.save()
                    messages.success(
                        request,
                        f"Emission {form.instance.title} successfully created!"
                        )
                    return HttpResponseRedirect(reverse('emissions'))
                else:
                    error = []
                    for field in form:
                        if field is not None:
                            error += field.errors
                    messages.error(request, error)
            else:
                messages.error(
                    request,
                    "Incorrect image format. Please upload jpg, "
                    "jpeg, png, tiff or bmp")

    else:
        messages.warning(
            request,
            f"You do not have the necessary permissions "
            "to create a new emission.\n Please contact your"
            " system administrator.")
        return HttpResponseRedirect(reverse('emissions'))

    context = {'form': form}
    return render(request, 'add-emission.html', context)


