from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Course, Enrollment, Question, Choice, Submission
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import logging

logger = logging.getLogger(__name__)


# CourseListView
class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user = self.request.user
        courses = Course.objects.order_by('-total_enrollment')[:10]
        for course in courses:
            if user.is_authenticated:
                course.is_enrolled = Enrollment.objects.filter(user=user, course=course).exists()
        return courses


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_details_bootstrap.html'


def enroll(request, course_id):
    if request.method == 'POST':
        user = request.user
        course = get_object_or_404(Course, pk=course_id)
        
        # Create enrollment
        enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)
        
        if created:
            course.total_enrollment += 1
            course.save()
        
        return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course_id,)))


# Submit view to handle exam submission
def submit(request, course_id):
    # Get the current user and course object
    user = request.user
    course = get_object_or_404(Course, pk=course_id)
    
    # Get the enrollment object for the user and course
    enrollment = get_object_or_404(Enrollment, user=user, course=course)
    
    # Create a new submission object
    submission = Submission.objects.create(enrollment=enrollment)
    
    # Get the submitted answers from the request
    submitted_choices = request.POST.getlist('choice')
    
    # Add each selected choice to the submission
    for choice_id in submitted_choices:
        choice = get_object_or_404(Choice, pk=choice_id)
        submission.choices.add(choice)
    
    # Save the submission
    submission.save()
    
    # Redirect to the show_exam_result view with the submission id
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', 
                                       args=(course_id, submission.id)))


# Show exam result view
def show_exam_result(request, course_id, submission_id):
    # Get the course and submission objects
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Get all the choices submitted by the user
    submitted_choices = submission.choices.all()
    
    # Get all questions for this course
    lessons = course.lesson_set.all()
    total_score = 0
    max_score = 0
    
    # Calculate the score
    question_results = []
    for lesson in lessons:
        questions = lesson.question_set.all()
        for question in questions:
            max_score += question.grade
            
            # Get selected choices for this question
            selected_choice_ids = submitted_choices.filter(question=question).values_list('id', flat=True)
            
            # Check if the answer is correct
            is_correct = question.is_get_score(selected_choice_ids)
            
            if is_correct:
                total_score += question.grade
            
            # Store question result info
            question_results.append({
                'question': question,
                'selected_choices': submitted_choices.filter(question=question),
                'is_correct': is_correct
            })
    
    # Calculate percentage
    if max_score > 0:
        percentage = (total_score / max_score) * 100
    else:
        percentage = 0
    
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'max_score': max_score,
        'percentage': percentage,
        'question_results': question_results,
        'lessons': lessons
    }
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)


# Authentication views
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'onlinecourse/user_registration_bootstrap.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                          password=password)
            login(request, user)
            return redirect("onlinecourse:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'onlinecourse/user_registration_bootstrap.html', context)


def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onlinecourse:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'onlinecourse/user_login_bootstrap.html', context)
    else:
        return render(request, 'onlinecourse/user_login_bootstrap.html', context)


def logout_request(request):
    logout(request)
    return redirect('onlinecourse:index')
