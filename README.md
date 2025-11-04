# Trivia Quizzler

A fun and interactive True/False trivia quiz application built using **Python** and **Tkinter**, with questions fetched from an online trivia API. The app keeps track of your score and provides instant feedback as you progress through the quiz.

---

## 🚀 Features

* ✅ Simple and clean UI using Tkinter
* ❓ True/False based quiz format
* 🔄 Fetches random trivia questions dynamically
* 🧠 Tracks and displays your score
* ✅ Visual feedback for correct & wrong answers
* 🎯 Automatically ends when questions are finished

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** (GUI library)
* **PyInstaller** for converting to `.exe`
* Trivia API for questions

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/kanikagoel688/trivia-quizzler.git
cd trivia-quizzler
```

---

## ▶️ How to Run

Run the script directly:

```bash
python main.py
```

or run the executable:

```bash
dist/Trivia-Quizzler.exe
```

---

## 🖼️ Screenshots

> <img width="431" height="707" alt="image" src="https://github.com/user-attachments/assets/21b1f576-8696-4e57-ab58-f7a03c215357" />


---

## 🔨 Build Executable (Optional)

Use PyInstaller:

```bash
pyinstaller --onefile --noconsole --add-data "images/true.png;images" --add-data "images/false.png;images" main.py
```

---

## 📁 Project Structure

```
Trivia-Quizzler/
│── images/
│   ├── true.png
│   └── false.png
│── data.py
│── main.py
│── quiz_brain.py
│── question_model.py
│── ui.py
│── README.md
```

---

## ✨ Future Enhancements

* More question categories 🏆
* Difficulty selection 🔥
* Sound effects 🎧
* Score history tracking 📊

---

## 🤝 Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

---

⭐ *If you like this project, please give it a star on GitHub!* 🌟
