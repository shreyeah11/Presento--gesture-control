# 🎯 Presento – Intuitive Hand Gesture Controller

Presento is a **computer vision–based system** that enables users to control **presentation slides and video playback** using intuitive **hand gestures**, eliminating the need for a keyboard or mouse.  
The project focuses on creating a **hands-free, natural interaction experience** using real-time gesture recognition.

---

## 🚀 Features

### 🎬 Presentation & Video Control
- **Start / Resume:** Open Palm  
- **Exit / Stop:** Closed Fist  

### 🔊 Volume Control
- **Increase Volume:** Thumbs Up  
- **Decrease Volume:** Thumbs Down  

### 💡 Brightness Control
- **Increase Brightness:** Thumb pointing right  
- **Decrease Brightness:** Thumb pointing left  

### 🧭 Navigation
- **Next Slide / +10s Video:** Moderate Swipe Right  
- **Previous Slide / −10s Video:** Moderate Swipe Left  

### ⏩ Video Playback
- **Fast Forward:** Fast Swipe Right  
- **Rewind:** Fast Swipe Left  

### 📜 Scrolling
- **Vertical Scrolling:** Pointing gesture  

---

## 🧠 Tech Stack

- **Python** — Core programming language  
- **OpenCV** — Real-time computer vision processing  
- **MediaPipe** — Hand landmark detection  
- **PyAutoGUI** — System-level input control  
- **NumPy** — Numerical computations  

---

## 📂 Folder Structure

```
presento-gesture-control/
├─ gesture_control/
│ ├─ main.py # Application entry point
│ ├─ gesture_recognition.py # Hand gesture detection logic
│ ├─ command_executor.py # Maps gestures to system actions
│ ├─ config.py # Configuration & thresholds
│ ├─ utils/ # Helper utilities
│ ├─ requirements.txt # Project dependencies
│ └─ README.md
├─ .gitignore
└─ README.md

```

---

## 🛠️ How to Run Locally

1️⃣ Clone the repository  
```bash
git clone https://github.com/shreyeah11/Presento-gesture-control.git
```
2️⃣ Navigate to the project directory
```
cd Presento-gesture-control/gesture_control
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```

4️⃣ Run the application
```
python main.py
```
---

## 🎯 Purpose of This Project

- Build a hands-free presentation control system  
- Apply computer vision concepts to a real-world problem  
- Explore gesture-based human–computer interaction  
- Develop a practical academic (PBL) project  
- Create an innovation-focused portfolio project  

---

## 🏆 Achievements

- Awarded **2nd Prize and Copyright** for *Presento* as part of a first-year Project-Based Learning (PBL) program  

---

## ✨ Future Enhancements

- Add gesture customization  
- Improve gesture accuracy in low-light conditions  
- Integrate voice feedback  
- Extend support to additional media players  

