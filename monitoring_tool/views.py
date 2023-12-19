from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Emission, EmissionCheck
from .forms import (
    EmissionSubmissionForm,
    EmissionCloseOutForm,
    CheckSubmissionForm,
    CheckEditForm)
from datetime import timedelta, datetime, timezone
from dateutil.relativedelta import relativedelta
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


class FirstMonday():
    """
    Class to contain private functions for calculating the first
    Monday of last, this and next month. These functions then feed
    into calculators for next and current check due dates.
    """
    # how to make functions class private from Stack Overflow:
    # https://stackoverflow.com/questions/61806295/how-to-define-method-in-class-that-can-only-be-called-from-init-method

    def __first_monday_current_month(self):
        """
        Function to calculate the first Monday of the current month
        and return this as a datetime object.
        """
        # how to access current month:
        # https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
        current_month = datetime.now().month
        current_year = datetime.now().year
        d = datetime(current_year, current_month, 7)
        offset = -d.weekday()  # weekday == 0 means Monday
        return d + timedelta(offset)

    def __first_monday_next_month(self):
        """
        Function to calculate the first Monday of next month and
        return this as a datetime object.
        """
        # how to access current month:
        # https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
        next_month_calc = datetime.now() + relativedelta(months=1)
        next_month = int(next_month_calc.strftime("%m"))
        year_plus_one_month = int(next_month_calc.strftime("%Y"))
        d = datetime(year_plus_one_month, next_month, 7)
        offset = -d.weekday()  # weekday == 0 means Monday
        return d + timedelta(offset)

    def __first_monday_last_month(self):
        """
        Function to calculate the first Monday of last month and
        return this as a datetime object.
        """
        # how to access current month:
        # https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python
        next_month_calc = datetime.now() - relativedelta(months=1)
        next_month = int(next_month_calc.strftime("%m"))
        year_plus_one_month = int(next_month_calc.strftime("%Y"))
        d = datetime(year_plus_one_month, next_month, 7)
        offset = -d.weekday()  # weekday == 0 means Monday
        return d + timedelta(offset)

    def calculate_next_check_due(self):
        """
        Function to calculate the next check due date using the
        current and next month functions above and working out
        which one to apply based on current date to ensure checks
        that fall between start of month and 1st Monday are not
        deemed to have expired erroneously.
        """
        first_monday_current_month = self.__first_monday_current_month()
        first_monday_next_month = self.__first_monday_next_month()
        now = datetime.now()
        if now < first_monday_current_month:
            return first_monday_current_month
        else:
            return first_monday_next_month

    def calculate_current_check_due(self):
        """
        Function to calculate the current check due date using the
        current and last month functions above and working out which
        one to apply based on current date to ensure checks that fall
        between start of month and 1st Monday are not deemed to have
        expired erroneously.
        """
        first_monday_current_month = self.__first_monday_current_month()
        first_monday_last_month = self.__first_monday_last_month()
        now = datetime.now()
        if now < first_monday_current_month:
            return first_monday_last_month
        else:
            return first_monday_current_month


class EmissionHome(generic.ListView):
    """
    Class for home page list view and filtered to show open
    emissions and ordered by created on field.
    """
    model = Emission
    queryset = Emission.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 20


class EmissionList(LoginRequiredMixin, generic.ListView):
    """
    Class for emissions page list view ordered by created on field.
    First Monday class is instantiated to update database with
    current and next check due dates.
    """
    # use of login required mixin to verify user is logged in before accessing
    # emissions and checks. This is if a non logged in user types in extension
    # into address bar. Solution from Stack Overflow:
    # https://stackoverflow.com/questions/61440990/how-to-check-whether-user-is-logged-in-or-not
    login_url = '/accounts/login/'
    model = Emission
    queryset = Emission.objects.order_by("-created_on")
    # update all emissions in the queryset with the current and next check due
    # using FirstMonday class and methods.
    first_monday = FirstMonday()
    queryset.update(
        current_check_due=first_monday.calculate_current_check_due()
        )
    queryset.update(
        next_check_due=first_monday.calculate_next_check_due()
        )
    template_name = "emissions.html"
    paginate_by = 20


class Emissions(View):
    """
    Class for emissions page view with get methods for getting, closing and
    deleting an emission.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Function to get emissions and return key data for use in
        the emission detail page. Checks that user is authenticated
        and if not returns them to the log in page.
        """
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
                'emission-detail.html',
                {
                    "title": title,
                    "description": description,
                    "image_url": image_url,
                    "location": location,
                    "slug": slug,
                    "created_on": created_on,
                    "check_complete": check_complete,
                    "status": status,
                    "type": type,
                    "last_checked": last_checked,
                    "next_check": next_check_due,
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
            # if not authenticated, direct to login page
            return redirect('/accounts/login')

    def close(request, slug, *args, **kwargs):
        """
        Function to close an emission, essentially allowing users
        to edit the emission. The emission slug is required to access
        the emission on the DB and on successful closure the user is
        returned to the emissions page. There is also error handling
        attached for form field errors. If the user does not have
        permissions the function raises a PermissionDenied exception.
        """
        queryset = Emission.objects
        emission = get_object_or_404(queryset, slug=slug)
        form = EmissionCloseOutForm()
        title = emission.title
        slug = emission.slug
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
                        # check that field has a value before proceeding.
                        # This is to prevent blank lines appearing in
                        # the alert.
                        if field is not None:
                            error += field.errors
                    messages.error(request, error)
        else:
            # raising a 403 error, solution from Stack Overflow:
            # https://stackoverflow.com/questions/51168730/which-exception-will-python-throw-when-it-does-not-have-sufficent-permissions-to
            raise PermissionDenied(
                "You do not have the necessary permissions "
                "to close an emission. Please contact your"
                " system administrator."
                )

        context = {'form': form, 'title': title, 'slug': slug}
        return render(request, 'close-emission.html', context)

    def delete(request, slug, *args, **kwargs):
        """
        Function to delete an emission provided user has the correct
        permission. The emission slug is required to access the
        emission on the DB and on successful deletion the user is
        returned to the emissions page. If the user does not have
        permissions the function raises a PermissionDenied exception.
        """
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
            raise PermissionDenied(
                "You do not have the necessary permissions "
                "to delete an emission."
                " Please contact your system administrator."
                )


def addEmission(request):
    """
    Function to add an emission provided user has the correct permission.
    The FirstMonday class is used to populate two fields in the form instance.
    There is logic to check upload image has the specified extension returning
    a message using messages framework with information for the user in an
    alert. Similarly, the form is checked for validity with errors again
    returned to user through messages framework. If the form submission was
    successful, the data is saved to DB and the user is informed of success
    again via messages whilst being redirected to the emissions page. If the
    user does not have permissions the function raises a PermissionDenied
    exception.
    """
    form = EmissionSubmissionForm()
    first_monday = FirstMonday()

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
                    form.instance.current_check_due = (
                        first_monday.calculate_current_check_due()
                        )
                    form.instance.next_check_due = (
                        first_monday.calculate_next_check_due()
                        )
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
        raise PermissionDenied(
            "You do not have the necessary permissions "
            "to add an emission. Please contact your"
            " system administrator."
            )

    context = {'form': form}
    return render(request, 'add-emission.html', context)


class EmissionCheckList(LoginRequiredMixin, generic.ListView):
    """
    Class for checks page list view ordered by date checked field.
    """
    # use of login required mixin to verify user is logged in before accessing
    # emissions and checks. This is if a non logged in user types in extension
    # into address bar. Solution from Stack Overflow:
    # https://stackoverflow.com/questions/61440990/how-to-check-whether-user-is-logged-in-or-not
    login_url = '/accounts/login/'
    model = EmissionCheck
    queryset = EmissionCheck.objects.order_by("-date_checked")
    template_name = "emission-checks.html"
    paginate_by = 20


def addCheck(request, slug):
    """
    Function to add a check provided user has the correct permission. The
    emission to check is first accessed using slug passed into function.
    The form is checked for validity with errors returned to user through
    messages framework. If the form submission is successful, the data is
    saved to DB and the user is informed of success again via messages
    whilst being redirected to the emission-checks page. If the user does
    not have permissions the function raises a PermissionDenied exception.
    """
    queryset = Emission.objects
    emission = get_object_or_404(queryset, slug=slug)
    form = CheckSubmissionForm()
    title = emission.title
    slug = emission.slug
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
                emission.last_checked = datetime.now()
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
        raise PermissionDenied(
            "You do not have the necessary permissions "
            f"to upload a new emission check for {title}."
            " Please contact your system administrator.")

    context = {'form': form, 'title': title, 'slug': slug}
    return render(request, 'add-check.html', context)


def deleteCheck(request, slug, id):
    """
    Function to delete a check provided user has the correct permission.
    The emission check is accessed using the id passed into the function.
    On successful deletion the user is returned to the emission-checks page
    whilst informing the user via the messages framework. If the user does
    not have permissions the function raises a PermissionDenied exception.
    """
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
        raise PermissionDenied(
            "You do not have the necessary permissions "
            f"to delete {emission_check.title} emission check."
            " Please contact your system administrator.")


def editCheck(request, slug, id):
    """
    Function to edit a check provided user has the correct permission. The
    check is first accessed using the id passed into function. A number of
    check variables are accessed, two of which are presented in the form
    and are available for edit. The other variables are used on form
    submission so that the original data is not lost. The form is checked
    for validity with errors returned to user through messages framework.
    If the form submission is successful, the data is saved to DB and the
    user is informed of success again via messages whilst being redirected
    to the emission-checks page. If the user does not have permissions the
    function raises a PermissionDenied exception.
    """
    emission_check_set = EmissionCheck.objects.all()
    emission_check = emission_check_set.get(id=id)
    title = emission_check.title
    check_id = emission_check.id
    checked_by = emission_check.checked_by
    status = emission_check.status
    check_date = emission_check.date_checked
    check_comments = emission_check.comments
    check_id = emission_check.id
    slug = emission_check.title.slug
    # adding data from SQL DB using code below, source Stack Overflow:
    # https://stackoverflow.com/questions/35134938/pass-database-value-in-form-django
    form = CheckEditForm(
        initial={'comments': check_comments, 'status': status}
        )
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
                form.instance.edited_by = (
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
        raise PermissionDenied(
            "You do not have the necessary permissions "
            f"to edit {emission_check.title} emission check. "
            "Please contact your system administrator."
            )

    context = {'form': form, 'title': title, 'id': check_id, 'slug': slug}
    return render(request, 'edit-check.html', context)
