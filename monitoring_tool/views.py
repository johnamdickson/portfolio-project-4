from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Emission, EmissionCheck
from .forms import EmissionSubmissionForm, EmissionCloseOutForm, CheckSubmissionForm, CheckEditForm
from datetime import timedelta, datetime, timezone
from dateutil.relativedelta import relativedelta
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

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


class EmissionHome(generic.ListView):
    model = Emission
    queryset = Emission.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 20


class EmissionList(LoginRequiredMixin, generic.ListView):
    # use of login required mixin to verify user is logged in before accessing 
    # emissions and checks. This is if a non logged in user types in extension into
    # address bar. Solution from Stack Overflow:
    # https://stackoverflow.com/questions/61440990/how-to-check-whether-user-is-logged-in-or-not
    login_url = '/accounts/login/'
    model = Emission
    queryset = Emission.objects.order_by("-created_on")
    queryset.update(next_check_due=first_monday_next_month())
    queryset.update(current_check_due=first_monday_current_month())
    template_name = "emission.html"
    paginate_by = 20



class Emissions(View):

    def get(self, request, slug, *args, **kwargs):
        # check if user is authenticated.
        if request.user.is_authenticated:
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
            javascript_data = emission.javascript_data
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
                    "javascript_data": javascript_data,
                },
            )
        else:
            # if not authenticate, direct to login page
            return render (request, 'account/login.html')


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
            # raising a 403 error, solution from Stack Overflow:
            # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
            raise PermissionDenied("You do not have the necessary permissions "
                "to close an emission. Please contact your"
                " system administrator.")

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
            # raising a 403 error, solution from Stack Overflow:
            # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
            raise PermissionDenied("You do not have the necessary permissions "
                "to delete an emission. Please contact your"
                " system administrator.")

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
                ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', 'webp')
                                        ):
                if form.is_valid():
                    form.instance.username = User.objects.get(
                                        username=request.user)
                    form.instance.current_check_due = first_monday_current_month()
                    form.instance.next_check_due = first_monday_next_month()
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
                    "jpeg, png, tiff, webp or bmp")

    else:
        # raising a 403 error, solution from Stack Overflow:
        # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
        raise PermissionDenied("You do not have the necessary permissions "
            "to add an emission. Please contact your"
            " system administrator.")

    context = {'form': form}
    return render(request, 'add-emission.html', context)


class EmissionCheckList(LoginRequiredMixin, generic.ListView):
    # use of login required mixin to verify user is logged in before accessing 
    # emissions and checks. This is if a non logged in user types in extension into
    # address bar. Solution from Stack Overflow:
    # https://stackoverflow.com/questions/61440990/how-to-check-whether-user-is-logged-in-or-not
    login_url = '/accounts/login/'
    model = EmissionCheck
    queryset = EmissionCheck.objects.order_by("-date_checked")
    template_name = "emission-checks.html"
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
                return HttpResponseRedirect(reverse('emission-checks'))
            else:
                error = []
                for field in form:
                    if field is not None:
                        error += field.errors
                messages.error(request, error)
    else:
        # raising a 403 error, solution from Stack Overflow:
        # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
        raise PermissionDenied("You do not have the necessary permissions "
            f"to upload a new emission check for {title}. Please contact your"
            " system administrator.")

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
            f" {emission_check.title} check has been deleted."
            )
        return HttpResponseRedirect(reverse('emission-checks'))
    else:
        # raising a 403 error, solution from Stack Overflow:
        # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
        raise PermissionDenied("You do not have the necessary permissions "
            f"to delete {emission_check.title} emission check. Please contact your"
            " system administrator.")

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
                    f"{emission_check.title} check has been edited."
                    )
                return HttpResponseRedirect(reverse('emission-checks'))
            else:
                error = []
                for field in form:
                    if field is not None:
                        error += field.errors
                messages.error(request, error)
    else:
        # raising a 403 error, solution from Stack Overflow:
        # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
        raise PermissionDenied("You do not have the necessary permissions "
            f"to edit {emission_check.title} emission check. Please contact your"
            " system administrator.")
    
    context = {'form': form, 'title': title}
    return render(request, 'edit-check.html', context)
