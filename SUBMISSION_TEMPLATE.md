# Assignment Submission Template

Use this template when submitting your assignment. Replace `tadagbe98` with your actual GitHub username.

---

## Task 1: models.py (3 points)
**GitHub URL:**
```
https://github.com/tadagbe98/django-online-course-project/blob/main/onlinecourse/models.py
```

**What to verify:**
- ✅ Question model with lesson FK, question_text, and grade fields
- ✅ Choice model with question FK, choice_text, and is_correct fields
- ✅ Submission model with enrollment FK and choices M2M relationship
- ✅ is_get_score() method in Question model

---

## Task 2: admin.py (3 points)
**GitHub URL:**
```
https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/admin.py
```

**What to verify:**
- ✅ Seven imported classes: Course, Lesson, Instructor, Learner, Question, Choice, Submission
- ✅ QuestionInline class (StackedInline)
- ✅ ChoiceInline class (StackedInline)
- ✅ QuestionAdmin class with ChoiceInline
- ✅ LessonAdmin class with QuestionInline

---

## Task 3: Admin Site Screenshot (1 point)
**Screenshot filename:** `03-admin-site.png`

**What to include in screenshot:**
- ✅ "Authentication and Authorization" section (Groups, Users)
- ✅ "OnlineCourse" section with all 7 models
- ✅ Full browser window showing the URL
- ✅ Clear, unblurred image

**How to take:**
1. Login to http://127.0.0.1:8000/admin/
2. Make sure you can see both sections on the page
3. Take full-page screenshot
4. Save as `03-admin-site.png`

---

## Task 4: course_details_bootstrap.html (2 points)
**GitHub URL:**
```
https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html
```

**What to verify:**
- ✅ Displays course name and description
- ✅ Shows all lessons using Django template tags ({% for lesson in course.lesson_set.all %})
- ✅ Displays questions with choices as checkboxes
- ✅ Bootstrap styling (Bootstrap 4 classes)
- ✅ Form with action pointing to submit view

---

## Task 5: views.py (2 points)
**GitHub URL:**
```
https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/views.py
```

**What to verify:**
- ✅ submit() function that:
  - Gets enrollment
  - Creates Submission object
  - Adds selected choices to submission
  - Redirects to show_exam_result
- ✅ show_exam_result() function that:
  - Gets course and submission
  - Calculates score
  - Evaluates each question
  - Passes results to template

---

## Task 6: urls.py (2 points)
**GitHub URL:**
```
https://github.com/YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/urls.py
```

**What to verify:**
- ✅ Path for submit: `path('course/<int:course_id>/submit/', views.submit, name='submit')`
- ✅ Path for show_exam_result: `path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result')`

---

## Task 7: Exam Result Screenshot (2 points)
**Screenshot filename:** `07-final.png`

**What to include in screenshot:**
- ✅ "Congratulations" message (should appear for score ≥ 80%)
- ✅ Score display showing points earned (e.g., "50/50 (100%)")
- ✅ Exam results section showing questions
- ✅ Green checkmarks (✓) for correct answers
- ✅ Full page or enough to see congratulations + score + some results

**How to take:**
1. Register as a student (not admin)
2. Enroll in your course
3. Take the exam (select all CORRECT answers)
4. Submit exam
5. Take screenshot of result page
6. Save as `07-final.png`

**Sample correct answers for the demo course:**
- Q1: "x = 5"
- Q2: "int", "str", "list" (all three)
- Q3: "for", "while" (both)
- Q4: "Exits the current loop"
- Q5: "def"

---

## Quick Checklist Before Submission

### URLs Ready:
- [ ] Task 1: models.py URL copied
- [ ] Task 2: admin.py URL copied
- [ ] Task 4: course_details_bootstrap.html URL copied
- [ ] Task 5: views.py URL copied
- [ ] Task 6: urls.py URL copied

### Screenshots Ready:
- [ ] Task 3: 03-admin-site.png saved
- [ ] Task 7: 07-final.png saved

### GitHub Repository:
- [ ] Repository is PUBLIC
- [ ] All code files pushed to GitHub
- [ ] Repository name: django-online-course-project

### Testing:
- [ ] Admin site accessible
- [ ] Can create course/lessons/questions
- [ ] Can register and login
- [ ] Can take exam
- [ ] Exam results display correctly

---

## Submission Steps

1. Go to the assignment page
2. Click "Begin the Assignment"
3. For each task, paste the corresponding GitHub URL or upload screenshot
4. Review all submissions
5. Click "Submit assignment"
6. Wait for AI evaluation

**Expected Score: 15/15 points (100%)**

---

## Example Submission Format

When you paste URLs in the assignment, they should look like this (with YOUR actual username):

**Example for Task 1:**
```
https://github.com/johnsmith/django-online-course-project/blob/main/onlinecourse/models.py
```

**NOT like this:**
```
YOUR_USERNAME/django-online-course-project/blob/main/onlinecourse/models.py
```

---

## Need Help?

If you're having issues:
1. Check SETUP_GUIDE.md for detailed instructions
2. Review README.md for troubleshooting
3. Make sure all files are in correct locations
4. Verify repository is public
5. Test all functionality before submitting

**Good luck! 🚀**
