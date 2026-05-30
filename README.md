# 🍎 Fruit Catcher

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pygame](https://img.shields.io/badge/Pygame-Game_Development-green)
![Status](https://img.shields.io/badge/Status-In_Development-orange)

Fruit Catcher là một game arcade được phát triển bằng Python, Pygame, OpenCV and MediaPipe.

Fruit Catcher là một trò chơi arcade sử dụng camera để tương tác không chạm (Touchless Interaction). Người chơi điều khiển giỏ bằng chuyển động bàn tay để bắt các loại trái cây rơi từ trên xuống nhằm ghi điểm, đồng thời tránh các quả bom xuất hiện ngẫu nhiên trong quá trình chơi.

Dự án được xây dựng với mục tiêu nghiên cứu và thực hành các kiến thức về:

* Game Programming
* Object-Oriented Programming (OOP)
* State Machine
* Event-Driven Architecture
* Observer Pattern
* Collision Detection
* Computer Vision
* Hand Tracking

---

## 🎮 Gameplay

* Điều khiển giỏ bằng chuyển động bàn tay thông qua camera.
* Bắt trái cây để tăng điểm.
* Tránh bom để không bị mất điểm hoặc kết thúc trò chơi.
* Hệ thống UI tương tác không chạm.
* Âm thanh nền và hiệu ứng âm thanh.
* Gameplay đơn giản, dễ tiếp cận và có khả năng mở rộng.

---

## 🛠️ Tech Stack

* Python 3.10
* Pygame
* OpenCV
* MediaPipe
* Object-Oriented Programming (OOP)

---

## ✨ Features

### Core Architecture

* Game Manager
* State Machine
* Event System
* Observer Pattern
* System-Based Architecture

### Gameplay

* Fruit Spawn System
* Bomb Spawn System
* Score Management
* Difficulty Scaling
* Object Lifecycle Management

### Input & Vision

* Camera Input bằng OpenCV
* Hand Tracking bằng MediaPipe
* Coordinate Mapping từ Camera Space sang Game Space
* Touchless Interaction

### Rendering

* Sprite Rendering
* UI Rendering
* Camera Overlay Rendering
* Layer-Based Rendering

### Audio

* Background Music
* Sound Effects
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
│   ├── event_type.py
│   ├── game_manager.py
│   ├── game_state.py
│   └── observer.py
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

## 🏗️ Architecture Overview

Dự án được tổ chức theo hướng **System-Based Architecture**, trong đó **Game Manager** đóng vai trò điều phối trung tâm và quản lý toàn bộ vòng đời của trò chơi.

```text
                 Game Manager
                       │
                (State Machine Control)
                       │
        ┌──────────────┬──────────────┐
        ▼              ▼              ▼
   Input System   Gameplay System   UI System
        │              │              │
        └───────┬──────┴──────┬───────┘
                       ▼            
                 Collision System
                       │
                       ▼
                 Render System
                       │
                       ▼
                  Audio System

Vision System
      │
      ▼
Input System
```

---

## Core Components

### Game Manager

Game Manager là thành phần điều phối trung tâm của toàn bộ hệ thống.

Chịu trách nhiệm:

* Khởi tạo các System
* Điều phối vòng lặp chính của game
* Quản lý Game State
* Điều khiển luồng xử lý giữa các System
* Quản lý vòng đời trò chơi

---

### State Machine

State Machine quản lý trạng thái hiện tại của game.

Ví dụ:

```text
MENU
 ↓
PLAYING
 ↓
PAUSE
 ↓
GAME_OVER
 ↓
QUIT
```

Mọi quyết định chuyển đổi trạng thái đều được thực hiện thông qua Game Manager.

---

### Event System & Observer Pattern

Cho phép các thành phần trong hệ thống giao tiếp với nhau mà không phụ thuộc trực tiếp vào nhau.

Ví dụ:

```text
Fruit Collected
        │
        ▼
 Gameplay System
        │
        ▼
 Publish Event
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
UI    Audio  Score
```

Kiến trúc này giúp giảm coupling giữa các thành phần và tăng khả năng mở rộng của dự án.

---

### Vision System

Chịu trách nhiệm:

* Nhận dữ liệu từ camera
* Xử lý hình ảnh bằng OpenCV
* Phát hiện bàn tay bằng MediaPipe
* Trích xuất vị trí fingertip

---

### Input System

Chịu trách nhiệm:

* Chuyển đổi dữ liệu từ Vision System thành dữ liệu đầu vào của game
* Mapping tọa độ từ Camera Space sang Game Space
* Cung cấp dữ liệu đầu vào cho Gameplay System và UI System

---

### Gameplay System

Chịu trách nhiệm:

* Spawn Fruit
* Spawn Bomb
* Quản lý Score
* Quản lý Difficulty
* Cập nhật trạng thái Game Object

Gameplay System không quản lý Game State.

---

### Collision System

Chịu trách nhiệm xử lý va chạm giữa:

* Basket và Fruit
* Basket và Bomb

---

### Render System

Chịu trách nhiệm hiển thị:

* Background
* Game Objects
* UI Components
* Camera Overlay

Render System quyết định thứ tự hiển thị của các thành phần trong game.

---

### Audio System

Chịu trách nhiệm:

* Background Music
* Sound Effects
* Audio Resource Management
* Volume Control

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone <repository-url>
cd Fruit-catcher
```

### 2. Create Virtual Environment (Python 3.10)

```bash
py -3.10 -m venv .venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Sau khi kích hoạt thành công:

```bash
(.venv)
```

sẽ xuất hiện ở đầu dòng lệnh.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run The Game

```bash
python main.py
```

---

## 🎯 Learning Objectives

Dự án được xây dựng nhằm thực hành và nghiên cứu:

* Python Programming
* Game Development Fundamentals
* Pygame Framework
* Object-Oriented Design
* State Machine
* Event-Driven Architecture
* Observer Pattern
* Collision Detection
* Asset Management
* Computer Vision
* Hand Tracking với MediaPipe

---

## 📸 Demo

Có thể bổ sung:

* Gameplay GIF
* Screenshots
* Architecture Diagram

sau khi dự án hoàn thiện.

---

## 👨‍💻 Tác giả

Dự án của nhóm 2 thành viên được phát triển nhằm nghiên cứu và thực hành quy trình phát triển game, kiến trúc phần mềm và các công nghệ xử lý tương tác bằng camera trong môi trường Python.
