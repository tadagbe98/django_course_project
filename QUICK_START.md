# 🚀 Quick Start Guide - Django Online Course Project

## ⚡ Fast Setup (5 Minutes)

### 1. Download & Extract
Download the `django_course_project` folder and extract it.

### 2. Install & Setup
```bash
cd django_course_project

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# OR Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install django pillow

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Username: admin
# Password: admin123

# Start server
python manage.py runserver
```

### 3. Create Sample Data
1. Visit http://127.0.0.1:8000/admin/
2. Login with admin/admin123
3. Create: Instructor → Course → Lessons → Questions → Choices

### 4. Test Application
1. Go to http://127.0.0.1:8000/
2. Register as student
3. Enroll in course
4. Take exam
5. View results

---

## 📸 Screenshots Needed

### Screenshot 1: `03-admin-site.png`
- URL: http://127.0.0.1:8000/admin/
- Show: Authentication + OnlineCourse sections
- Take: Full page screenshot

### Screenshot 2: `07-final.png`
- Complete an exam with 100% score
- Show: Congratulations + Score + Results
- Take: Full page screenshot

---

## 🔗 GitHub Submission URLs

After pushing to GitHub, get these URLs:

1. **models.py**: `https://github.com/USERNAME/REPO/blob/main/onlinecourse/models.py`
2. **admin.py**: `https://github.com/USERNAME/REPO/blob/main/onlinecourse/admin.py`
3. **course_details_bootstrap.html**: `https://github.com/USERNAME/REPO/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
4. **views.py**: `https://github.com/USERNAME/REPO/blob/main/onlinecourse/views.py`
5. **urls.py**: `https://github.com/USERNAME/REPO/blob/main/onlinecourse/urls.py`

---

## 📋 Assignment Checklist

- [ ] Create GitHub repository (PUBLIC)
- [ ] Push all code to GitHub
- [ ] Take `03-admin-site.png`
- [ ] Take `07-final.png` (with 100% score)
- [ ] Get 5 GitHub URLs
- [ ] Submit all URLs and screenshots
- [ ] Score: 15/15 points ✨

---

## 🎯 Key Features Implemented

✅ **Models**: Question, Choice, Submission
✅ **Admin**: QuestionInline, ChoiceInline, QuestionAdmin, LessonAdmin
✅ **Views**: submit(), show_exam_result()
✅ **URLs**: Exam submission and result paths
✅ **Templates**: Bootstrap-styled course details and exam results
✅ **Functionality**: Complete exam workflow with scoring

---

## ⚠️ Common Issues

**Issue**: Can't access admin
**Fix**: Run `python manage.py createsuperuser`

**Issue**: Images not showing
**Fix**: Check MEDIA_URL in settings.py

**Issue**: Module not found
**Fix**: Activate virtual environment

**Issue**: Not getting 100% score
**Fix**: Select ONLY correct answers

---

## 📚 Detailed Guides

- **SETUP_GUIDE.md** - Complete step-by-step setup
- **SUBMISSION_TEMPLATE.md** - Submission format and checklist
- **README.md** - Full project documentation

---

## 🎓 Ready to Submit!

1. Follow Quick Setup above
2. Create sample course with questions
3. Take both screenshots
4. Push to GitHub
5. Submit URLs and screenshots
6. Get full marks! 🌟

**Need help?** Check the detailed guides in the project folder.

**Good luck! 🚀**
