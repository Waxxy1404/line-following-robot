# 🤖 Line Following Robot — CoppeliaSim Simulation

A computer vision-based line following robot simulated in **CoppeliaSim**, using a Pioneer P3-DX mobile robot with a Kinect RGB camera. The robot detects a line on the ground through image processing and autonomously adjusts its wheel speeds to follow it in real time.

---

## 📋 Overview

This project implements a **proportional visual controller** for a differential-drive robot. A virtual camera captures grayscale frames from the simulated environment, detects the position of a dark line using pixel intensity thresholding, and calculates the centroid of the detected line. The robot's left and right motor velocities are then adjusted proportionally to keep the line centered in its field of view.

---

## ✨ Features

- 🎥 Real-time image acquisition from a simulated Kinect RGB camera
- 🔍 Line detection via grayscale pixel intensity thresholding
- 📐 Centroid calculation for precise line position estimation
- ⚙️ Proportional differential speed control (no PID library needed)
- 🔄 Memory of last known direction when line is temporarily lost
- 🖥️ Live camera feed visualization with OpenCV

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python 3 | Main programming language |
| CoppeliaSim | Robot simulation environment |
| sim (CoppeliaSim Remote API) | Communication between Python and simulator |
| OpenCV (`cv2`) | Image display and processing |
| NumPy | Image array manipulation |
| PIL (Pillow) | Image handling support |

---

## 🤖 Robot & Simulation Setup

| Component | Details |
|---|---|
| Robot Model | Pioneer P3-DX (differential drive) |
| Camera | Kinect RGB (`kinect_rgb`) — grayscale mode |
| Left Motor | `Pioneer_p3dx_leftMotor` |
| Right Motor | `Pioneer_p3dx_rightMotor` |
| Connection | Remote API via TCP — `127.0.0.1:19997` |

---

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────┐
│                  CoppeliaSim                    │
│                                                 │
│   ┌──────────┐    Camera Frame    ┌──────────┐  │
│   │ Kinect   │ ────────────────► │ Pioneer  │  │
│   │  RGB     │                   │  P3-DX   │  │
│   └──────────┘                   └──────────┘  │
└─────────────────────────────────────────────────┘
          │                              ▲
          │ image (via Remote API)       │ motor velocities
          ▼                              │
┌─────────────────────────────────────────────────┐
│                 Python Script                   │
│                                                 │
│  1. Capture grayscale frame                     │
│  2. Threshold dark pixels (intensity < 32)      │
│  3. Calculate centroid X of detected line       │
│  4. Map centroid → differential wheel speed     │
│  5. Send velocity commands to both motors       │
└─────────────────────────────────────────────────┘
```

### Control Logic

The motor speed is calculated proportionally based on where the line appears in the camera frame:

```python
left_speed  = 1.4 * (2 * coord / resolution[0])
right_speed = 1.4 * (2 * (resolution[0] - coord) / resolution[0])
```

- Line on the **left** → left motor faster → robot turns left
- Line on the **right** → right motor faster → robot turns right
- Line **centered** → both motors at equal speed → robot goes straight
- Line **not detected** → robot continues with last known direction

---

## 🚀 Getting Started

### Prerequisites

- [CoppeliaSim](https://www.coppeliarobotics.com/) (formerly V-REP) installed
- Python 3.x
- CoppeliaSim Remote API files (`sim.py`, `simConst.py`, `remoteApi` library) in the project folder

### Install Python Dependencies

```bash
pip install numpy opencv-python pillow
```

### Running the Project

1. Open **CoppeliaSim**

2. Load the simulation scene:
   - Go to **File → Open Scene**
   - Select `scenes/line_following.ttt`

3. Start the simulation by clicking ▶️ in CoppeliaSim

4. Run the Python script in a separate terminal:

```bash
python Projeto_0_victor.py
```

5. A window labeled `CAMERA DO ROBO SIMULADO` will open showing the robot's live camera feed

> ⚠️ **Important:** Always start the CoppeliaSim simulation **before** running the Python script, otherwise the Remote API connection will fail.

---

## 📁 Project Structure

```
line-following-robot/
├── Projeto_0_victor.py     # Main control script
├── sim.py                  # CoppeliaSim Remote API
├── simConst.py             # CoppeliaSim constants
├── remoteApi.dll           # Remote API library (Windows)
├── scenes/
│   └── line_following.ttt  # CoppeliaSim simulation scene
└── README.md
```

---

## 🎓 Context

This project was developed as part of a **Digital Processing of Images** course at **UFPE (Universidade Federal de Pernambuco)**. It demonstrates the integration of visual perception and motor control in a simulated robotic environment — a foundational concept in autonomous mobile robotics.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Victor Hugo Camurça**
- GitHub: [@Waxxy1404](https://github.com/Waxxy1404)
- LinkedIn: [victor-hugo-camurça](https://linkedin.com/in/victor-hugo-camurça)
