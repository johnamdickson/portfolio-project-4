from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Emission, EmissionCheck
from .forms import EmissionSubmissionForm, EmissionCloseOutForm, CheckSubmissionForm, CheckEditForm
from datetime import timedelta, datetime, timezone
from dateutil.relativedelta import relativedelta


class EmissionHome(generic.ListView):
    model = Emission
    queryset = Emission.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 20


class EmissionList(generic.ListView):

    def first_monday_current_month():
        # how to access current month:
        # https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
        current_month = datetime.now().month
        current_year = datetime.now().year
        d = datetime(current_year, current_month, 7)
        offset = -d.weekday() # weekday == 0 means Monday
        return d + timedelta(offset)
    
    def first_monday_next_month():
        # how to access current month:
        # https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
        next_month_calc = datetime.now() + relativedelta(months=1)
        next_month = int(next_month_calc.strftime("%m"))
        year_plus_one_month = int(next_month_calc.strftime("%Y"))
        d = datetime(year_plus_one_month, next_month, 7)
        offset = -d.weekday() # weekday == 0 means Monday
        return d + timedelta(offset)

    model = Emission
    queryset = Emission.objects.order_by("-created_on")
    queryset.update(next_check_due=first_monday_next_month())
    queryset.update()
    template_name = "emission.html"
    paginate_by = 20



        # # how to access next month:
        # # https://stackoverflow.com/questions/21145618/how-do-i-find-the-nth-day-of-the-next-month-in-python
        # next_month_calc = datetime.now() + relativedelta(months=1)
        # next_month = int(next_month_calc.strftime("%m"))
        # print(next_month)
        # # first_monday_current_month = 
        # return f"Current Month is {current_month} next month is {next_month}"


class Emissions(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Emission.objects
        emission = get_object_or_404(queryset, slug=slug)
        title = emission.title
        description = emission.description
        image_url = emission.emission_image.url
        location = emission.location
        created_on = emission.created_on
        type = emission.get_emission_type
        status = emission.calculate_status
        check_complete = emission.calculate_check_complete
        last_checked = emission.last_checked
        next_check_due = emission.next_check_due
        current_check_due = emission.current_check_due
        close_out_comments = emission.close_out_comments
        closed_by = emission.closed_by
        close_out_date = emission.close_out_date
        latitude = emission.latitude
        longitude = emission.longitude
        return render(
            request,
            'emission_detail.html',
            {
                "title": title,
                "description": description,
                "image_url": image_url,
                "location": location,
                "slug": slug,
                "created_on": created_on,
                "check_complete": check_complete,
                "status": status,
                "type" : type,
                "last_checked": last_checked,
                "next_check" : next_check_due,
                "current_check": current_check_due,
                "close_out_comments": close_out_comments,
                "closed_by": closed_by,
                "close_out_date": close_out_date,
                "latitude": latitude,
                "longitude": longitude,
            },
        )

    def close(request, slug, *args, **kwargs):
        queryset = Emission.objects
        emission = get_object_or_404(queryset, slug=slug)
        form = EmissionCloseOutForm()
        title = emission.title
        # check if user has permissions to add emissions ie emission admin.
        if request.user.has_perm('monitoring_tool.change_emission'):
            if request.method == 'POST':
                # issue uploading image to DB from html form.
                # Solution from Stack Overflow:
                # https://stackoverflow.com/questions/45912825/image-upload-field-works-in-django-admin-but-not-working-in-template
                form = EmissionCloseOutForm(request.POST, instance=emission)
                if form.is_valid():
                    form.instance.closed_by = (
                        f'{User.objects.get(username=request.user)}')
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
                        # check that field has a value before proceeding. This is to prevent 
                        # blank lines appearing in the alert.
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

        context = {'form': form, 'title': title}
        return render(request, 'close-emission.html', context)

    def delete(request, slug, *args, **kwargs):
        queryset = Emission.objects
        emission = get_object_or_404(queryset, slug=slug)
        if request.user.has_perm('monitoring_tool.delete_emission'):
            emission.delete()
            messages.info(
                request,
                f" {emission.title} has been deleted."
                )
            return HttpResponseRedirect(reverse('emissions'))
        else:
            messages.warning(
                request,
                f"You do not have the necessary permissions "
                "to delete an emission.\n Please contact your"
                " system administrator.")
            return HttpResponseRedirect(reverse('emissions'))

def addEmission(request):
    form = EmissionSubmissionForm()
    # check if user has permissions to add emissions ie emission admin.
    # issue uploading image to DB from html form.
    # Solution from Stack Overflow:
    # https://stackoverflow.com/questions/45912825/image-upload-field-works-in-django-admin-but-not-working-in-template

    if request.user.has_perm('monitoring_tool.add_emission'):
        if request.method == 'POST':
            form = EmissionSubmissionForm(request.POST, request.FILES)
            # access form image name from request.FILES and use conditional 
            # code to proceed or generate error message.
            form_images = request.FILES.getlist('emission_image', None)
            form_image = form_images[0]
            if str(form_image).endswith(
                ('.jpg', '.jpeg', '.png', '.tiff', '.bmp')
                                        ):
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


class EmissionCheckList(generic.ListView):
    model = EmissionCheck
    queryset = EmissionCheck.objects.order_by("-date_checked")
    template_name = "emission_checks.html"
    paginate_by = 20

    

def addCheck(request, slug):
    queryset = Emission.objects
    emission = get_object_or_404(queryset, slug=slug)
    form = CheckSubmissionForm()
    title = emission.title
    # check if user has permissions to add check.
    if request.user.has_perm('monitoring_tool.add_emissioncheck'):
        if request.method == 'POST':
            form = CheckSubmissionForm(request.POST)
            # access form image name from request.FILES and use conditional 
            # code to proceed or generate error message.
            if form.is_valid():
                form.instance.title = emission
                form.instance.date_checked = datetime.now()
                # update the emission last checked data to now. Solution from 
                # stack overflow:
                # https://stackoverflow.com/questions/70683436/updating-data-in-a-model-from-views-django
                emission.last_checked=datetime.now()
                emission.save()
                form.instance.checked_by = User.objects.get(
                                    username=request.user)
                form.save()
                messages.success(
                    request,
                    f"{form.instance.title} check successfully uploaded!"
                    )
                return HttpResponseRedirect(reverse('emission_checks'))
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
            "to upload a new emission check.\n Please contact your"
            " system administrator.")
        return HttpResponseRedirect(reverse('emission_checks'))

    context = {'form': form, 'title': title}
    return render(request, 'add-check.html', context)


def deleteCheck(request, slug, id):
    emission_check_set = EmissionCheck.objects.all()
    emission_check = emission_check_set.get(id=id)
    check_id = emission_check.id
    if request.user.has_perm('monitoring_tool.change_emissioncheck'):
        emission_check.delete()
        messages.info(
            request,
            f" {emission_check.title} check number {check_id} has been deleted."
            )
        return HttpResponseRedirect(reverse('emission_checks'))
    else:
        messages.warning(
            request,
            f"You do not have the necessary permissions "
            "to delete an emission check.\n Please contact your"
            " system administrator.")
        return HttpResponseRedirect(reverse('emission_checks'))

def editCheck(request, slug, id):
    emission_check_set = EmissionCheck.objects.all()
    emission_check = emission_check_set.get(id=id)
    title = emission_check.title
    check_id = emission_check.id
    checked_by = emission_check.checked_by
    status = emission_check.status
    check_date = emission_check.date_checked
    check_comments = emission_check.comments
    check_id = emission_check.id
    # adding data from SQL DB using code below, source Stack Overflow:
    # https://stackoverflow.com/questions/35134938/pass-database-value-in-form-django
    form = CheckEditForm(initial={'comments': check_comments, 'status': status})
    print(checked_by)
    print(check_comments)
    # check if the current user matches the person who submitted the check
    # only allowing this person and superuser to edit. Check for superuser
    # code from stack overflow:
    # https://stackoverflow.com/questions/65421561/how-can-i-check-if-an-user-is-superuser-in-django
    if request.user == emission_check.checked_by or request.user.is_superuser:
        if request.method == 'POST':
            form = CheckEditForm(request.POST)
            if form.is_valid():
                form.instance.id = check_id
                form.instance.date_checked = check_date
                form.instance.title = title
                form.instance.checked_by = checked_by
                form.instance.edited_by =(
                    f'{User.objects.get(username=request.user)}')
                form.instance.edit_date = datetime.now()
                form.save()
                messages.success(
                    request,
                    f"{emission_check.title} check number {check_id} has been edited."
                    )
                return HttpResponseRedirect(reverse('emission_checks'))
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
            "to edit this check.\n Please contact your"
            " system administrator.")
        return HttpResponseRedirect(reverse('emission_checks'))
    
    context = {'form': form, 'title': title}
    return render(request, 'edit-check.html', context)
