#  Image Upload / Download & Management Web App ---- ImageIQ AI

**ImageIQ** is an web application for image processing and analysis. It allows users to upload images, apply transformations, and extract meaningful insights efficiently.

## Screenshots

![Demo_ScreenShots](https://github.com/jahidhasanpiyesh/ImageIQ/blob/main/static/Demo.png)  

**Live Demo:** [Click here to view live](https://imageiq.pythonanywhere.com)

## Features

- **User Authentication:** Secure signup and login system  
- **Image Upload:** Users can upload images with a title and additional info  
- **Search & Query:** Other users can search images based on title, tags, or info  
- **Image Download:** Users can download images shared by others according to their needs  
- **Real-Time Updates:** Instant availability of uploaded images for search and download  
- **User-Friendly Interface:** Clean, responsive UI for easy navigation and interaction  
- **Metadata Management:** Titles and info help organize and query images efficiently  


## Tech Stack

- **Backend:** Python 3.x, Django 5.2.8  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default)  
- **Environment & Config:** `python-dotenv` for environment variables, `tzdata` for timezone management  
- **Dependencies:**  
  - `asgiref==3.11.0` (ASGI support for Django)  
  - `pillow==12.0.0` (image handling)  
  - `sqlparse==0.5.3` (SQL parsing for Django)  
  - `python-dotenv==1.2.1` (load environment variables)  
- **Deployment:** PythonAnywhere  

> Note: No OpenCV or heavy AI libraries are used; the project relies on Django and Pillow for image handling.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ImageIQ.git
cd ImageIQ
```

## Create and activate virtual environment:

- python -m venv env
- source env/bin/activate  # Linux/Mac
- env\Scripts\activate     # Windows

## Install dependencies:

- pip install -r requirements.txt

## Run migrations:
* python manage.py migrate

## Open in browser: http://127.0.0.1:8000/
## Usage:

- Sign up or login

- Upload images for processing

- View processed results in real-time

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

### 2️⃣ Save & Zip

1. Open a text editor and paste the above into a file named `README.md`.  
2. Save it in your project folder (`ImageIQ`).  
3. On **Windows**: Right-click the folder → Send to → Compressed (zipped) folder  
   On **Linux/Mac**:  

```bash
zip -r ImageIQ.zip ImageIQ/
```
**Author:** Md Jahid Hasan – Python Backend Developer | Open to Collaboration  
**Contact / Portfolio:** [https://jahidhasanpiyesh.github.io/portfolio/index.html]   
