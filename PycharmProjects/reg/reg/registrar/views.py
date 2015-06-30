from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q # advanced filtering

# Import all of the app's models
from registrar.models import *

# Create your views here.

# Recall: a view is a function that takes a request (HttpRequest) and
# returns a response (HttpResponse)

def course_detail(request, course_id):
    # course = Course.objects.get(id=course_id)
    # get_object_or_404 will query the database for an object of that ID
    # and return an Http 404 (not found) if that ID is invalid
    course = get_object_or_404(Course, pk=course_id)
    
    #text = '''Department: %s
#Number: %d
#Title: %s''' % (course.dept, course.number, course.title)
    #return HttpResponse(text, content_type='text/plain')

    # The reverse() function reverses a URL from urls.py. I.e., given the name
    # of a view (the name= part in urls.py), it generates a URL for that view.
    # I need to specify professor_id because that is a required parameter of the view.
    inst_detail_url = reverse('professor_detail',
        kwargs={ 'professor_id': course.instructor.id })
    
    context = {
        'dept': course.dept,
        'number': course.number,
        'title': course.title,
        'instructor': course.instructor,
        'inst_detail_url': inst_detail_url,
    }
    
    # render parameters:
    #   the request,
    #   the name of the template (file),
    #   the context (dictionary containing substitutions)
    return render(request, 'course_detail.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    context = {
        'id': student.id,
        'fname': student.fname,
        'lname': student.lname,
        'birthdate': student.birthdate,
        'email': student.email,
    }
    
    return render(request, 'student_detail.html', context)
    
def professor_detail(request, professor_id):
    prof = get_object_or_404(Professor, pk=professor_id)
    # Fetch the prof's courses in order of department and number
    courses = prof.course_set.order_by('dept', 'number')
    
    context = {
        'prof': prof,
        'courses': courses,
    }
    
    return render(request, 'professor_detail.html', context)
    
def course_list(request):
    # request contains a dictionary called GET that contains all the key-value pairs
    # passed through GET
    
    if 'search_string' in request.GET:
        # Display just the courses containg the search string
        # title__icontains: title contains whatever, case-insensitive
        search = request.GET['search_string']
        courses = Course.objects \
            .filter(Q(title__icontains=search) \
                | Q(dept__icontains=search) \
                | Q(number__contains=search)) \
            .order_by('dept', 'number')
    else:
        # courses is a list of all the Course objects in my database
        courses = Course.objects.order_by('dept', 'number')
        search = None
    
    context = {
        'courses': courses,
        'search': search,
    }
    
    return render(request, 'course_list.html', context)
    
def professor_list(request):
    if 'search_string' in request.GET:
        search = request.GET['search_string']
        profs = Professor.objects \
            .filter(Q(fname__icontains=search) | Q(lname__icontains=search)) \
            .order_by('lname', 'fname')
    else:
        profs = Professor.objects.order_by('lname', 'fname')
        search = None
    
    context = {
        'profs': profs,
        'search': search,
    }
    
    return render(request, 'professor_list.html', context)

def index(request):
    context = {
    }
    
    return render(request, 'index.html', context)
    
    
    
    
    
    