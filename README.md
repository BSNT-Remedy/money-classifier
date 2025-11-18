# **PesoScan — Django + Teachable Machine Image Classification**

PesoScan is a Django web application that integrates a **Teachable Machine (TF.js) image model** to classify Philippine peso bills in real time using a webcam or uploaded images. The system supports **user authentication, prediction storage, analytics dashboards**, and includes a **Model Card** and **Ethics Statement** for responsible AI usage.

---

## 🔗 **Live Demo**
Try the app here: [PesoScan Demo](https://peso-scan.onrender.com/)

---

## 🚀 **Features**

### 🔍 **Image Classification (Client-Side Inference)**
- Uses **TensorFlow.js + Teachable Machine**  
- Realtime webcam-based classification  
- Displays **prediction + confidence score**  

### 🧾 **Prediction Storage**
- Saves predictions (label + confidence + user) to database  
- Stored under **user account**, separated per user  
- Admin can view all data

### 📊 **Analytics Dashboard**
- Counts per label  
- Average confidence per label  
- Total predictions  
- Works only for authenticated users  

### 👤 **User Authentication**
- Register  
- Login / Logout  
- Role-ready model (Guest, User, Admin)

### 📄 **Model Card & Ethics Statement**
- Contains model dataset summary  
- Limitations and risks  
- Proper usage guidelines  
- Ethical considerations

---

## 🛠 **Tech Stack**

**Backend:** Django 4+ (Python 3.10+)  
**Front-end:** Django Templates  
**ML Model:** Teachable Machine (TensorFlow.js) — Image model  
**Database:** SQLite  
**Inference Method:** Client-side (TF.js)

---

## 📁 **Project Structure**
```
project/
│── core/                  # Django project folder
│── main/                  # Application
│   ├── models.py          # Prediction model
│   ├── views.py           # Prediction logic + Analytics
│   ├── templates/         # HTML templates
│   ├── static/            # Model + JS files
│   ├── urls.py
│── static/
│   ├── model.json
│   ├── weights.bin
│   ├── metadata.json
```

---

## ⚙️ **Installation**

### **1. Clone the repository**
```bash
git clone https://github.com/yourusername/pesoscan.git
cd pesoscan
```

### **2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run migrations**
```bash
python manage.py migrate
```

### **5. Run development server**
```bash
python manage.py runserver
```

---

## 📷 **How It Works**

### **1. Capture**
User opens the home page → webcam turns on.

### **2. Classify**
ML5.js loads the Teachable Machine model → predicts the peso bill.

### **3. Save**
User clicks **Save Prediction** → stored in DB under their account.

### **4. Analyze**
Users view their prediction history and analytics (charts + stats).

---

## 🔐 **User Roles**

| Role | Permissions |
|------|-------------|
| Guest | View homepage only |
| Authenticated User | Classify + Save + View Analytics |
| Admin | Can view all users' predictions |

---

## 🧠 **Model Card**

A full model card is included at `/model-card/` describing:
- Dataset used (classes, number of samples)
- Training process
- Intended use
- Limitations
- Performance notes  

---

## ⚖️ **Ethics Statement**

The ethics page at `/ethics/` covers:
- Model bias warnings  
- Responsible usage  
- Privacy considerations  
- Proper deployment guidelines  
- Avoiding misuse in financial or security contexts  

---


