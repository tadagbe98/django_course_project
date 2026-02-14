from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# QuestionInline class - allows adding questions inline within a lesson
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


# ChoiceInline class - allows adding choices inline within a question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# QuestionAdmin class - register Question with ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson', 'grade']
    list_filter = ['lesson__course']
    search_fields = ['question_text']


# LessonAdmin class - register Lesson with QuestionInline
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'course', 'order']
    list_filter = ['course']


# CourseAdmin class
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date', 'total_enrollment']
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# EnrollmentAdmin class  
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'date_enrolled', 'mode']
    list_filter = ['course', 'mode']


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
