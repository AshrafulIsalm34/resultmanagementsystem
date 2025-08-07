

# 🎓 Django Result Management System

This is a Django-based web application for managing and displaying student results, including subject-wise GPA, semester GPA, and overall CGPA. It uses OOP principles such as inheritance, encapsulation, abstraction, and polymorphism to maintain clean and modular code.

## 🚀 Features

- Student Signup & Login System
- Add Multiple Subjects with Marks for One Student ID per Semester
- Search Result by Student ID and Semester
- View Result as Modern Stylish Cards (JS & CSS powered)
- Per Subject GPA, Semester GPA, and Overall CGPA Calculation
- Delete Individual Result Cards (with JS)
- Admin Panel for Full Control

## 🧱 Tech Stack

- **Backend:** Django 5.2.4 (Python 3.13.5)
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Database:** SQLite (Development)
- **PDF Export:** xhtml2pdf / WeasyPrint / wkhtmltopdf (as per setup)
- **Environment Management:** python-dotenv

## 🧰 Setup Instructions

### 🔧 Clone the Repository

```bash
git clone https://github.com/AshrafulIslam34/result-management-system.git
cd result-management-system
```

### 🐍 Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ⚙️ Set Environment Variables

Create a `.env` file in the root directory:

```
DJANGO_ENV=development
SECRET_KEY=your-secret-key
DEBUG=True
```

### 🛠️ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 👤 Create Superuser

```bash
python manage.py createsuperuser
```

### ▶️ Run Server

```bash
python manage.py runserver
```

Then open: `http://127.0.0.1:8000`

---

## 🧪 Test Users

You can use the admin panel at `/admin` to add or manage users, students, subjects, and results.

---

## ✨ Deployment Notes

- Use `DJANGO_ENV=production` in `.env` for live servers.
- Configure `ALLOWED_HOSTS` dynamically in `settings.py` using the ENV variable.
- Use a proper production-ready database and media storage.

---

## 👨‍💻 Author

Developed by **Ashraful Islam**

---

## 📄 License

This project is licensed under the MIT License.