# Django Online Course Application - Final Project

## Project Overview
This is a Django-based online course application with exam functionality. Students can enroll in courses, view lessons, take exams, and see their results.

## Features Implemented

### Task 1: Models (models.py)
- **Question Model**: Stores exam questions with grade points
- **Choice Model**: Stores answer choices for each question with is_correct flag
- **Submission Model**: Tracks student exam submissions and selected answers

### Task 2: Admin Configuration (admin.py)
- **QuestionInline**: Add questions inline when editing lessons
- **ChoiceInline**: Add choices inline when editing questions
- **QuestionAdmin**: Manage questions with choice inlines
- **LessonAdmin**: Manage lessons with question inlines
- Seven imported classes: Course, Lesson, Instructor, Learner, Question, Choice, Submission

### Task 3: Admin Site
- Full admin interface configured with all models
- Authentication and Authorization section
- OnlineCourse section with all models

### Task 4: Course Details Template (course_details_bootstrap.html)
- Displays course name, image, and description
- Shows all lessons with content
- Displays exam questions with checkboxes for multiple choice
- Bootstrap styling for responsive design

### Task 5: Views (views.py)
- **submit()**: Handles exam submission, creates Submission object, saves choices
- **show_exam_result()**: Calculates score, evaluates answers, displays results

### Task 6: URLs (urls.py)
- Path for submit: `/course/<int:course_id>/submit/`
- Path for show_exam_result: `/course/<int:course_id>/submission/<int:submission_id>/result/`

### Task 7: Exam Result Template
- Shows congratulations message for passing (≥80%)
- Displays total score and percentage
- Shows detailed results for each question
- Highlights correct and incorrect answers

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repository
```bash
git clone <your-github-repo-url>
cd django_course_project
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django
pip install pillow  # For image handling
```

### Step 4: Create Django Project Structure
If not already created:
```bash
django-admin startproject mysite .
python manage.py startapp onlinecourse
```

### Step 5: Configure Settings
Add to `mysite/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'onlinecourse',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Step 6: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser
```bash
python manage.py createsuperuser
# Enter username, email, and password
```

### Step 8: Run the Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Creating Sample Data

### Using Admin Site (http://127.0.0.1:8000/admin/)

1. **Login** with superuser credentials

2. **Create an Instructor**:
   - Click "Add Instructor"
   - Select a user
   - Set full_time and total_learners

3. **Create a Course**:
   - Click "Add Course"
   - Enter name, description, pub_date
   - Upload an image
   - Select instructors

4. **Create Lessons** (in Course or separately):
   - Click "Add Lesson"
   - Enter title, order, content
   - Select course

5. **Create Questions** (in Lesson or separately):
   - Click "Add Question"
   - Enter question text
   - Set grade points
   - Add multiple choices
   - Mark correct answer(s)

6. **Add Choices** (when creating Question):
   - Enter choice text
   - Check "is_correct" for correct answers
   - Add at least 2-4 choices per question

## Usage Flow

1. **Student Registration/Login**
   - Register new account or login
   
2. **Browse Courses**
   - View available courses on homepage
   
3. **Enroll in Course**
   - Click on course to view details
   - Click "Enroll" button
   
4. **View Course Content**
   - Read lessons
   - Review course materials
   
5. **Take Exam**
   - Scroll to exam section
   - Select answers (checkboxes)
   - Click "Submit Exam"
   
6. **View Results**
   - See overall score and percentage
   - View congratulations message if passed
   - Review detailed answer feedback
   - See which answers were correct/incorrect

## File Structure
```
django_course_project/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── onlinecourse/
│   ├── migrations/
│   ├── templates/
│   │   └── onlinecourse/
│   │       ├── course_details_bootstrap.html
│   │       └── exam_result_bootstrap.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/  # Course images stored here
└── manage.py
```

## GitHub Submission Guide

### For Task Submissions:

**Task 1**: Submit URL to `models.py`
- Example: `https://github.com/yourusername/project/blob/main/onlinecourse/models.py`

**Task 2**: Submit URL to `admin.py`
- Example: `https://github.com/yourusername/project/blob/main/onlinecourse/admin.py`

**Task 4**: Submit URL to `course_details_bootstrap.html`
- Example: `https://github.com/yourusername/project/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html`

**Task 5**: Submit URL to `views.py`
- Example: `https://github.com/yourusername/project/blob/main/onlinecourse/views.py`

**Task 6**: Submit URL to `urls.py`
- Example: `https://github.com/yourusername/project/blob/main/onlinecourse/urls.py`

### For Screenshot Tasks:

**Task 3**: Take screenshot of admin site showing:
- Authentication and Authorization section
- OnlineCourse section
- Save as `03-admin-site.png`

**Task 7**: Take screenshot of exam result showing:
- Congratulations message
- Score display
- Exam results
- Save as `07-final.png`

## Testing the Application

1. Create a course with 2-3 lessons
2. Add 3-5 questions per lesson
3. Add 3-4 choices per question
4. Mark correct answers
5. Enroll as a student
6. Take the exam
7. Submit and view results

## Troubleshooting

### Images not showing:
- Check MEDIA_URL and MEDIA_ROOT in settings.py
- Ensure images are uploaded in admin

### Admin site not accessible:
- Run: `python manage.py createsuperuser`
- Check that 'django.contrib.admin' is in INSTALLED_APPS

### Migrations errors:
- Delete db.sqlite3
- Delete migrations folder (except __init__.py)
- Run: `python manage.py makemigrations`
- Run: `python manage.py migrate`

## Grading Criteria Checklist

- [x] Task 1: models.py with Question, Choice, Submission (3 points)
- [x] Task 2: admin.py with 7 classes and inlines (3 points)
- [x] Task 3: Admin site screenshot (1 point)
- [x] Task 4: course_details_bootstrap.html (2 points)
- [x] Task 5: views.py with submit and show_exam_result (2 points)
- [x] Task 6: urls.py with exam paths (2 points)
- [x] Task 7: Final exam result screenshot (2 points)

**Total: 15 points**

## License
This project is for educational purposes as part of a Django course final project.
