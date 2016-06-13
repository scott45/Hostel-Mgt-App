from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from Gyobera.forms import UserForm, UserProfileForm
from django.shortcuts import redirect
from Gyobera.models import Classification
from Gyobera.models import List
from Gyobera.models import Student
from Gyobera.models import Booking
from Gyobera.models import Room
from Gyobera.forms import ClassificationForm
from Gyobera.forms import MobilePaymentForm
from Gyobera.forms import BookForm
from Gyobera.forms import ListForm
from Gyobera.forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from Gyobera.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context


def home(request):
    return render(request, 'home.html')


def payment(request):
    if request.method == "POST":
        form = MobilePaymentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = MobilePaymentForm()
    return render(request, 'gyobera/payment.html', {'form': form})


def index(request):
    classification_list = Classification.objects.order_by('-likes')[:6]
    list_list = List.objects.order_by('-views')[:5]
    context_dict = {'classifications': classification_list, 'lists': list_list}
    return render(request, 'index.html', context_dict)


def about(request):
    return render(request, 'about.html', {})


def gallery(request):
    return render(request, 'Gallery.html', {})


def booking(request):
    context_dict = {}
    context = RequestContext(request)
    booking_list = Booking.objects.all()
    for booking in booking_list:
        context_dict = {'bookings': booking_list}
    return render_to_response('gyobera/view_bookings.html', context_dict, context)


def classification(request, classification_name_slug):
    context_dict = {}
    try:
        classification = Classification.objects.get(slug=classification_name_slug)
        context_dict['classification_name'] = classification.name
        context_dict['classification_name_slug'] = classification_name_slug
        lists = List.objects.filter(classification=classification).order_by('-views')
        context_dict['lists'] = lists
    except Classification.DoesNotExist:
        return render(request, 'gyobera/classification.html', context_dict)


def registry(request):
    context_dict = {}
    context = RequestContext(request)
    student_list = Student.objects.all()
    for student in student_list:
        context_dict = {'students': student_list}
    return render_to_response('gyobera/registry.html', context_dict, context)


def rooms(request):
    context_dict = {}
    context = RequestContext(request)
    room_list = Room.objects.all()
    for room in room_list:
        context_dict = {'rooms': room_list}
    return render_to_response('gyobera/room.html', context_dict, context)


def add_classification(request):
    if request.method == "POST":
        form = ClassificationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = ClassificationForm()
    return render(request, 'gyobera/add_classification.html', {'form': form})


def book(request):
    # check if user has already booked:
    has_booked = Booking.objects.filter(Booked_by_id=request.POST.get('booked_by')).exists()
    # are room free?
    rooms_full = Booking.objects.count() == 40
    if rooms_full or has_booked:
        # redirect to a error view
        return 'You have reserved yourself a room'

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = BookForm()
    return render(request, 'gyobera/book_now.html', {'form': form})


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = StudentForm()
    return render(request, 'gyobera/student.html', {'form': form})


def add_list(request, classification_name_slug):
    try:
        cat = Classification.objects.get(slug=classification_name_slug)
    except Classification.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            if cat:
                list = form.save(commit=False)
                list.classification = cat
                list.views = 0
                list.title = 100
                list.Custodian = 100
                list.description = 200
                list.save()
                # probably better to use a redirect here.
                return classification(request, classification_name_slug)
        else:
            print(form.errors)
    else:
        form = ListForm()

    context_dict = {'form': form, 'classification': cat}

    return render(request, 'gyobera/add_list.html', context_dict)


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = \
                get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )

            email.send()
            return redirect('contact')

    return render(request, 'gyobera/contact_form.html', {
        'form': form_class,
    })


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('gyobera/register.html',
                              {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                              context)


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/Gyobera/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Gyobera account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'gyobera/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("You are logged in, proceed!")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Gyobera/')


def track_url(request):
    url = '/Gyobera/'
    if request.method == 'GET':
        if 'list_id' in request.GET:
            list_id = request.GET['list_id']
            try:
                list = List.objects.get(id=list_id)
                list.views += 1
                list.save()
                url = list.url
            except:
                pass

    return redirect(url)
