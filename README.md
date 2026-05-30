# 🍎 Fruit Catcher
# 🍎 Fruit Catcher

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pygame](https://img.shields.io/badge/Pygame-Game_Development-green)
![Status](https://img.shields.io/badge/Status-In_Development-orange)

Fruit Catcher là một game arcade được phát triển bằng Python và Pygame.

Người chơi điều khiển một chiếc giỏ để bắt các loại trái cây rơi từ trên xuống nhằm ghi điểm. Bên cạnh đó, các quả bom sẽ xuất hiện ngẫu nhiên và cần được tránh để không bị mất điểm hoặc kết thúc trò chơi.

Dự án được xây dựng với mục tiêu học tập và thực hành các kiến thức về Game Programming, Object-Oriented Programming (OOP), Game Architecture, Collision Detection, Asset Management và Real-Time System Design.

---

## 🎮 Gameplay

* Bắt trái cây để ghi điểm.
* Tránh bom để không bị trừ điểm.
* Hệ thống tính điểm theo thời gian thực.
* Background Music và Sound Effects.
* Gameplay đơn giản, dễ tiếp cận.
* Kiến trúc được chia thành nhiều System độc lập để dễ mở rộng và bảo trì.

---

## 🛠️ Công nghệ sử dụng

* Python 3.10
* Pygame
* OpenCV
* MediaPipe
* Object-Oriented Programming (OOP)

---

## ✨ Tính năng chính

### Gameplay

* Fruit Spawn System
* Bomb Spawn System
* Score Management
* Difficulty Scaling
* Game State Management

### Input & Vision

* Camera Input bằng OpenCV
* Hand Tracking bằng MediaPipe
* Chuyển đổi tọa độ từ Camera Space sang Game Space
* Hỗ trợ điều khiển không chạm (Touchless Interaction)

### Rendering

* Render Sprite
* Render UI
* Render Camera Overlay
* Layer-based Rendering

### Audio

* Background Music
* Sound Effects
* Audio Cache System
* Volume Control

---

## 📂 Project Structure

```text
Fruit-catcher/
│
├── Assets/
│   ├── Images/
│   └── Sounds/
│
├── Core/
│
├── Mocks/
│
├── Models/
│
├── Systems/
│   ├── Audio/
│   ├── Collision/
│   ├── GamePlay/
│   ├── Input/
│   ├── Render/
│   ├── UI/
│   └── Vision/
│
├── Utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🏗️ Kiến trúc hệ thống

Dự án được tổ chức theo hướng System-Based Architecture.

```text
Camera Input
        │
        ▼
Vision System
        │
        ▼
Input System
        │
 ┌──────┴──────┐
 ▼             ▼
UI System   Gameplay System
      │       │
      └───┬───┘
          ▼
  Collision System
          ▼
    Render System
          ▼
     Audio System
```

### Vision System

Chịu trách nhiệm nhận dữ liệu từ camera, xử lý hình ảnh và phát hiện vị trí bàn tay thông qua MediaPipe.

### Input System

Chuyển đổi dữ liệu từ Vision System thành dữ liệu đầu vào thống nhất để Gameplay System và UI System có thể sử dụng.

### Gameplay System

Quản lý toàn bộ logic gameplay:

* Spawn Fruit
* Spawn Bomb
* Quản lý Score
* Quản lý Level
* Điều khiển Game State

### Collision System

Xử lý va chạm giữa:

* Cursor và UI
* Basket và Fruit
* Basket và Bomb

### Render System

Chịu trách nhiệm hiển thị toàn bộ nội dung của trò chơi:

* Background
* Game Objects
* UI Components
* Camera Overlay

### Audio System

Quản lý:

* Background Music
* Sound Effects
* Volume Settings
* Audio Resources

---

## 🚀 Hướng dẫn chạy dự án

### 1. Clone repository

```bash
git clone <repository-url>
cd Fruit-catcher
```

### 2. Tạo Virtual Environment bằng Python 3.10

```bash
py -3.10 -m venv .venv
```

### 3. Kích hoạt Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Sau khi kích hoạt thành công sẽ xuất hiện:

```bash
(.venv)
```

ở đầu dòng lệnh.

### 4. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 5. Chạy game

```bash
python main.py
```

---

## 🎯 Mục tiêu học tập

Dự án được xây dựng nhằm thực hành và nghiên cứu:

* Python Programming
* Game Development Fundamentals
* Pygame Framework
* Object-Oriented Design
* Game Architecture
* Collision Detection
* Event-Driven Systems
* Asset Management
* Camera-based Interaction
* Hand Tracking với MediaPipe

---

## 📸 Demo

Có thể bổ sung hình ảnh hoặc GIF gameplay tại đây sau khi dự án hoàn thiện.

---

## 👨‍💻 Tác giả

Dự án của nhóm 2 thành viên được phát triển nhằm nghiên cứu và thực hành quy trình phát triển game, kiến trúc phần mềm và các công nghệ xử lý tương tác bằng camera trong môi trường Python.
