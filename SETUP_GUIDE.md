# Complete Setup Guide for Django Online Course Project

## Table of Contents
1. [Initial Setup](#initial-setup)
2. [Running the Application](#running-the-application)
3. [Creating Sample Data](#creating-sample-data)
4. [Taking Required Screenshots](#taking-required-screenshots)
5. [GitHub Setup and Submission](#github-setup-and-submission)
6. [Assignment Submission Checklist](#assignment-submission-checklist)

---

## Initial Setup

### Step 1: Install Python and Git
Make sure you have Python 3.8+ and Git installed on your computer.

```bash
# Check Python version
python --version

# Check Git version
git --version
```

### Step 2: Create Project Directory and Virtual Environment

```bash
# Create a directory for your project
mkdir django_course_project
cd django_course_project

# Create virtual environment
# On Windows:
python -m venv venv
venv\Scripts\activate

# On Mac/Linux:
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Django and Pillow

```bash
pip install django
pip install pillow
```

### Step 4: Create Django Project Structure

```bash
# Create Django project
django-admin startproject mysite .

# Create onlinecourse app
python manage.py startapp onlinecourse
```

### Step 5: Copy All Project Files

Copy all the files from the provided project folder to your `django_course_project` directory. Make sure the structure looks like this:

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
│   │       ├── course_list_bootstrap.html
│   │       ├── course_details_bootstrap.html
│   │       ├── exam_result_bootstrap.html
│   │       ├── user_registration_bootstrap.html
│   │       └── user_login_bootstrap.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```

### Step 6: Run Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser

# Enter the following:
# Username: admin
# Email: admin@example.com
# Password: admin123
# Password (again): admin123
```

---

## Running the Application

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
- Main site: http://127.0.0.1:8000/
- Admin site: http://127.0.0.1:8000/admin/

---

## Creating Sample Data

### Step 1: Login to Admin Site

1. Visit http://127.0.0.1:8000/admin/
2. Login with your superuser credentials (admin/admin123)

### Step 2: Create an Instructor

1. Click on "Add" next to "Instructors"
2. Select the admin user you created
3. Check "Full time"
4. Enter "100" for Total learners
5. Click "Save"

### Step 3: Create a Course

1. Click on "Add" next to "Courses"
2. Fill in the details:
   - **Name**: "Introduction to Python Programming"
   - **Description**: "Learn Python from basics to advanced concepts with hands-on coding exercises"
   - **Pub date**: Select today's date
   - **Total enrollment**: 50
3. For the image, download any course-related image from the internet and upload it
4. Select the instructor you created
5. Click "Save"

### Step 4: Create Lessons with Questions

**Lesson 1: Python Basics**

1. Click on "Add" next to "Lessons"
2. Fill in:
   - **Title**: "Python Basics"
   - **Order**: 1
   - **Course**: Select "Introduction to Python Programming"
   - **Content**: "This lesson covers variables, data types, and basic operations in Python."

3. Add questions inline:

   **Question 1:**
   - **Question text**: "What is the correct way to declare a variable in Python?"
   - **Grade**: 10
   
   Add choices:
   - ☐ "int x = 5"
   - ☑ "x = 5" (check "is_correct")
   - ☐ "var x = 5"
   - ☐ "variable x = 5"

   **Question 2:**
   - **Question text**: "Which of the following are valid Python data types?"
   - **Grade**: 10
   
   Add choices:
   - ☑ "int" (check "is_correct")
   - ☑ "str" (check "is_correct")
   - ☑ "list" (check "is_correct")
   - ☐ "var"

4. Click "Save"

**Lesson 2: Control Flow**

1. Click "Add" next to "Lessons"
2. Fill in:
   - **Title**: "Control Flow"
   - **Order**: 2
   - **Course**: Select "Introduction to Python Programming"
   - **Content**: "Learn about if statements, loops, and conditional logic."

3. Add questions:

   **Question 3:**
   - **Question text**: "What keyword is used to create a loop in Python?"
   - **Grade**: 10
   
   Add choices:
   - ☐ "loop"
   - ☑ "for" (check "is_correct")
   - ☑ "while" (check "is_correct")
   - ☐ "repeat"

   **Question 4:**
   - **Question text**: "What does the 'break' statement do?"
   - **Grade**: 10
   
   Add choices:
   - ☑ "Exits the current loop" (check "is_correct")
   - ☐ "Skips to the next iteration"
   - ☐ "Creates a new loop"
   - ☐ "Pauses the program"

4. Click "Save"

**Lesson 3: Functions**

1. Click "Add" next to "Lessons"
2. Fill in:
   - **Title**: "Functions"
   - **Order**: 3
   - **Course**: Select "Introduction to Python Programming"
   - **Content**: "Understanding how to create and use functions in Python."

3. Add question:

   **Question 5:**
   - **Question text**: "Which keyword is used to define a function in Python?"
   - **Grade**: 10
   
   Add choices:
   - ☐ "function"
   - ☑ "def" (check "is_correct")
   - ☐ "func"
   - ☐ "define"

4. Click "Save"

---

## Taking Required Screenshots

### Task 3: Admin Site Screenshot (03-admin-site.png)

1. Make sure you're logged into the admin site (http://127.0.0.1:8000/admin/)
2. You should see two main sections:
   - **Authentication and Authorization** (Groups, Users)
   - **Onlinecourse** (Choices, Courses, Enrollments, Instructors, Learners, Lessons, Questions, Submissions)
3. Take a full-page screenshot showing both sections
4. Save it as `03-admin-site.png`

**Tips for taking the screenshot:**
- Windows: Use Snipping Tool or Win + Shift + S
- Mac: Use Command + Shift + 4
- Make sure both sections are clearly visible
- Don't crop out the browser header showing the URL

### Task 7: Exam Result Screenshot (07-final.png)

To get this screenshot, you need to actually take and pass the exam:

1. **Register a new user** (not the admin):
   - Go to http://127.0.0.1:8000/
   - Click "Sign Up"
   - Create a new account (e.g., username: student1, password: student123)

2. **Enroll in the course**:
   - After registration, you'll be redirected to the homepage
   - Click on "Introduction to Python Programming"
   - Click the "Enroll" button

3. **Take the exam**:
   - Scroll down to the "Course Exam" section
   - Answer all questions **correctly** to get a passing score:
     - Question 1: Select "x = 5"
     - Question 2: Select "int", "str", and "list"
     - Question 3: Select "for" and "while"
     - Question 4: Select "Exits the current loop"
     - Question 5: Select "def"
   - Click "Submit Exam"

4. **Take the screenshot**:
   - You should see the exam result page with:
     - **Congratulations message** ("🎉 Congratulations! You passed the exam! 🎉")
     - **Score**: 50/50 (100%)
     - **Detailed results** showing each question with correct/incorrect indicators
   - Take a full-page screenshot
   - Save it as `07-final.png`

**Important**: Make sure the screenshot shows:
- ✅ The congratulations message
- ✅ The score (should be 100% if you selected all correct answers)
- ✅ At least some of the question results with green checkmarks

---

## GitHub Setup and Submission

### Step 1: Create GitHub Repository

1. Go to https://github.com/
2. Login or create an account
3. Click the "+" icon in the top right
4. Select "New repository"
5. Enter repository name: `django-online-course-project`
6. Make it **Public** (required for submission)
7. Click "Create repository"

### Step 2: Initialize Git and Push Code

```bash
# Navigate to your project directory
cd django_course_project

# Initialize git repository
git init

# Create .gitignore file
echo "venv/
__pycache__/
*.pyc
db.sqlite3
media/
.DS_Store
*.log" > .gitignore

# Add all files
git add .

# Commit
git commit -m "Initial commit - Django Online Course Project"

# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/django-online-course-project.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Get GitHub URLs for Each File

After pushing, get the GitHub URLs for submission:

1. Go to your GitHub repository
2. Navigate to each file
3. Click "Raw" or copy the file's GitHub URL
4. The URL format should be:
   `https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/PATH/TO/FILE`

**Required URLs:**

- **Task 1 (models.py)**:
  ```
  https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/models.py
  ```

- **Task 2 (admin.py)**:
  ```
  https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/admin.py
  ```

- **Task 4 (course_details_bootstrap.html)**:
  ```
  https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html
  ```

- **Task 5 (views.py)**:
  ```
  https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/views.py
  ```

- **Task 6 (urls.py)**:
  ```
  https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/urls.py
  ```

---

## Assignment Submission Checklist

Before submitting, verify you have:

### Required GitHub URLs:
- [ ] Task 1: models.py GitHub URL
- [ ] Task 2: admin.py GitHub URL
- [ ] Task 4: course_details_bootstrap.html GitHub URL
- [ ] Task 5: views.py GitHub URL
- [ ] Task 6: urls.py GitHub URL

### Required Screenshots:
- [ ] Task 3: `03-admin-site.png` showing both sections
- [ ] Task 7: `07-final.png` showing congratulations, score, and results

### Code Verification:
- [ ] models.py includes Question, Choice, and Submission models
- [ ] admin.py has 7 imported classes
- [ ] admin.py includes QuestionInline, ChoiceInline, QuestionAdmin, LessonAdmin
- [ ] views.py has submit() and show_exam_result() functions
- [ ] urls.py has paths for submit and show_exam_result
- [ ] Templates display properly with Bootstrap styling

### Functionality Test:
- [ ] Can access admin site
- [ ] Can create courses, lessons, and questions
- [ ] Can register and login as a student
- [ ] Can enroll in a course
- [ ] Can take an exam
- [ ] Can see exam results with congratulations message

---

## Troubleshooting

### Problem: "Module not found" error
**Solution**: Make sure you activated your virtual environment

### Problem: Images not displaying
**Solution**: Check MEDIA_URL and MEDIA_ROOT in settings.py

### Problem: Can't access admin site
**Solution**: Make sure you ran `python manage.py migrate` and created a superuser

### Problem: Getting 404 errors
**Solution**: Check that URLs are properly configured in both mysite/urls.py and onlinecourse/urls.py

### Problem: Exam submission not working
**Solution**: Make sure you have questions with choices created in the admin

### Problem: Not getting 100% score
**Solution**: Make sure you selected ALL correct answers and ONLY correct answers for each question

---

## Final Notes

- Make sure your repository is **public** so graders can access it
- Double-check all GitHub URLs are correct before submitting
- Take clear, full-page screenshots
- Ensure screenshots show all required elements
- Test your application thoroughly before submission

**Good luck with your submission! 🎓**
