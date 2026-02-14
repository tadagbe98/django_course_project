import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.conf import settings
import uuid


# Instructor model
class Instructor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return self.user.username


# Learner model
class Learner(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    REQUIRED_FIELDS = ['first_name', 'last_name']
    occupation = models.CharField(null=True, max_length=20, choices=[
            ('student', 'Student'),
            ('developer', 'Developer'),
            ('data_scientist', 'Data Scientist'),
            ('dba', 'Database Admin')
        ])
    social_link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.user.username + "," + \
               self.occupation


# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=30, default='online course')
    image = models.ImageField(upload_to='course_images/')
    description = models.CharField(max_length=1000)
    pub_date = models.DateField(null=True)
    instructors = models.ManyToManyField(Instructor)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Enrollment')
    total_enrollment = models.IntegerField(default=0)
    is_enrolled = False

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


# Enrollment model
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    BETA = 'BETA'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
        (BETA, 'BETA')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
    rating = models.FloatField(default=5.0)


# Question model
class Question(models.Model):
    # Foreign key to lesson
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # Question text
    question_text = models.CharField(max_length=500)
    # Question grade/mark
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    # Check if a learner selected the correct answers for this question
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False


# Choice model
class Choice(models.Model):
    # Foreign key to question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Choice text
    choice_text = models.CharField(max_length=200)
    # Indicates if this choice is a correct answer or not
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


# Submission model
class Submission(models.Model):
    # Foreign key to enrollment
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    # Many-to-many relationship with choices
    choices = models.ManyToManyField(Choice)
    
    def __str__(self):
        return f"Submission by {self.enrollment.user.username} for {self.enrollment.course.name}"
