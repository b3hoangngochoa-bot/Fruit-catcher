# Fruit Catcher

Fruit Catcher là một mini game được phát triển bằng Python và Pygame. Người chơi điều khiển giỏ để bắt các loại trái cây rơi từ trên xuống nhằm ghi điểm, đồng thời tránh các quả bom để không bị trừ điểm hoặc kết thúc trò chơi.

Dự án được xây dựng nhằm mục đích học tập, thực hành lập trình game, quản lý asset, xử lý gameplay và tổ chức mã nguồn theo hướng đối tượng.

---

## Requirements

* Python 3.10
* pip

---

## Setup Environment

### 1. Clone repository

```bash
git clone <repository-url>
cd Fruit_Catcher
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Hoặc nếu máy có nhiều phiên bản Python:

```bash
py -3.10 -m venv .venv
```

### 3. Activate virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run The Game

Sau khi cài đặt hoàn tất, chạy entry point của dự án:

```bash
python main.py
```

> Nếu entry point của dự án sử dụng tên file khác, hãy thay `main.py` bằng file tương ứng.

---

## Project Structure

```text
Fruit_Catcher/
│
├── assets/          # Images, audio, fonts
├── src/             # Source code
├── requirements.txt
├── main.py
└── README.md
```

---

## Features

* Fruit spawning system
* Bomb spawning system
* Score tracking
* Sound effects and background music
* Object-oriented architecture
* Pygame rendering pipeline

---

## Development Notes

Dự án sử dụng:

* Python 3.10
* Pygame
* OpenCV (nếu được tích hợp)
* MediaPipe (nếu được tích hợp)

Khuyến nghị sử dụng đúng phiên bản Python 3.10 để đảm bảo khả năng tương thích với các thư viện được sử dụng trong dự án.

---

## Author

Developed as a learning project for studying game programming, gameplay systems, and software architecture using Python.
