# 🐶 MAXIE - Cartoon Dog & Task Manager 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pygame_Zero-FF6F61?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" />
</p>

<p align="center">
  <strong>A fun self-care app.</strong>
</p>

![Maxie UI screenshot](images/Screenshot%202025-12-26%20213658.png)

A fun, interactive app built in python using **Pygame Zero**. This project demonstrates how to create a simple User Interface with clickable checkboxes, sprite manipulation, and dynamic text rendering.

---

## 🌟 Features

- **Custom UI System**: Interactive chckboxes built from scratch using `Rect` collision logic.
- **Live Text Feedback**: Real-time tet rendering to display task status.
- **Environment Control**: Toggle background states and character properties through code-driven logic.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher
* `pip` (Python package installer)

### Instllation

1. **Clone the repository**
```bash
   git clone [https://github.com/josequiceno2000/cartoon-dog-manager.git](https://github.com/josequiceno2000/cartoon-dog-manager.git)
   cd cartoon-dog-manager
```

2. Activate your virtual Environment
```bash
    # Windows
    .venv\Scripts\activate

    # Mac/Linux
    source .venv/bin/activate
```
3. Install Pygame Zero
```bash
    pip install pgzero
```

---

## 📂 Project Structure

Pygame Zero relies on specific naming conventions for asset folders. Ensure your directory looks like this:

``` Plaintext
.
├── images/          # Assets (dog.png, checkbox.png, etc.)
├── fonts/           # Custom .ttf or .otf files
├── main.py          # Main application script
├── .gitignore       # Prevents tracking .venv and __pycache__
└── README.md        # Project documentation
```

---

## 🎮 Usage

To launch the app, run:

```bash
    python main.py
```

**Interactions**
- Mouse Click: Click the squares next to tasks to toggle them.

---
## 🛠️ Built With
- [Python](https://www.python.org/) - The programming language used.
- [Pygame Zero](https://pygame-zero.readthedocs.io/) - The wrapper library for easy graphics.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE&authuser=1) for more details.
