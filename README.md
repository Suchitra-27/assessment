# assessment
# Group Management System (Angular + FastAPI)


## Project Structure

### **Frontend (Angular)**
frontend/ │-- src/ │ │-- app/ │ │ │-- components/ │ │ │ │-- group/ │ │ │ │ │-- group.component.ts │ │ │ │ │-- group.component.html │ │ │ │ │-- group.component.css │ │-- app.module.ts │-- angular.json │-- package.json │-- README.md

### **Backend (FastAPI)**
backend/ │-- main.py │-- requirements.txt │-- README.md

---

## Installation

### **Backend (FastAPI) Setup**
1. **Install Python**

2. **Create a virtual environment** and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Run FastAPI server:
uvicorn main:app --reload
FastAPI will run at:
http://127.0.0.1:8000

Check API in browser or Postman:
----------------------------------------------------------------------------------
Frontend (Angular) Setup
Install Node.js & Angular CLI (if not installed):

Download Node.js
Install Angular CLI:
npm install -g @angular/cli
Navigate to frontend/ directory:

cd frontend
Install dependencies (node_modules): If the node_modules folder is missing, install dependencies using:

npm install
This will install all required packages listed in package.json.
If there are issues, try:

npm cache clean --force
npm install
Run Angular app:

ng serve
Angular will run at:
http://localhost:4200

