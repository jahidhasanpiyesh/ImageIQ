# 🖼️ Django Image Uploader & Downloader

A feature-rich Django web application that allows users to **upload**, **search**, **preview**, and **download** images. Built using Django's powerful form and model system, this project demonstrates how to handle media files securely, integrate user authentication, and implement real-time search features using Django QuerySets and Regex.

---

## 🌐 Live Demo

👉 [Visit Live Website](https://imgstoreandshare.pythonanywhere.com/)  
🔐 Login to explore all features (Upload & Download)

---

## 🚀 Features

- ✅ User registration, login, logout
- 📤 Upload images with title & description
- 🔍 Real-time search with Regex (title/description)
- 📥 Secure image downloads
- 🧩 Clean UI with Bootstrap 5
- 🛡️ Authenticated-only image interactions
- 🔔 Django message framework for notifications

---

## 🛠️ Tech Stack

| Category      | Technologies                      |
|---------------|-----------------------------------|
| Language      | Python 3                          |
| Framework     | Django 4.x                        |
| Frontend      | HTML5, CSS3, Bootstrap 5          |
| Database      | SQLite3 (default)                 |
| Hosting       | [PythonAnywhere](https://pythonanywhere.com) |
| File Uploads  | Django `ImageField` & media files |
| Authentication| Django built-in auth              |

---

## ⚙️ Getting Started

''' bash
# Clone the repository
git clone https://github.com/jahidhasanpiyesh/Django-Image-Uploader-Download.git

# Navigate into the directory
cd Django-Image-Uploader-Download

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

# Visit the app
http://127.0.0.1:8000/

---

📁 Project Structure
Django-Image-Uploader-Download/
│
├── imageuploader/             # Main app
│   ├── static/                # CSS/JS assets
│   ├── templates/             # HTML templates
│   ├── models.py              # Image model
│   ├── forms.py               # Upload form
│   └── views.py               # All views
│
├── media/                     # Uploaded images
├── requirements.txt
├── db.sqlite3
└── manage.py

---

📸 Screenshots

🏠 Home Page (Upload & Search)

🔎 Search Results

📥 Download Modal

---

🔮 Future Enhancements
🌍 Multi-user gallery with profiles

🧾 Pagination for image lists

🌫️ Drag & drop upload

📊 Upload/download counters

📂 Categorization by tags

----

🤝 Contributing
Want to contribute?

Fork the repo

Create a new branch

Commit changes

Push and create a Pull Request

---

👨‍💻 Author
Md. Jahid Hasan Piyesh
🎓 Python & Django Developer
🌐 GitHub
📧 Email: jahidhasanpiyesh@gmail.com

---

🌟 Support
If you like this project:

⭐️ Star it on GitHub
📢 Share it with others
🛠️ Suggest new features
