# Real-Time Telemetry Data Pipeline
A lightweight, real-time telemetry streaming pipeline built with **FastAPI** and **Streamlit**. This project streams dynamic telemetry metrics from an event producer into an in-memory cached backend, rendering live data visualization without WebSocket threading lockups or UI stutter.
---
## 🏗️ Architecture & System Overview

### Key Technical Features
* **In-Memory Cache Architecture:** Optimized backend endpoint (`/latest`) eliminates latency overhead and avoids WebSocket thread contention on Streamlit UI rerenders.
* **Simulated Telemetry Producer:** Background engine generating continuous system metrics with fault handling and configurable emission intervals.
* **Live Interactive Visualizations:** Dynamic metric displays, time-series charts, and status indicators built using Streamlit.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **Frontend / Dashboard:** Streamlit, Pandas, Requests
* **Data Processing:** Python `time`, `random`, `json`

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.9+
* `pip` package manager

### 2. Installation
Clone the repository and install required packages:
```bash
git clone [https://github.com/sharanya-ks19/realtime-telemetry-pipeline.git](https://github.com/sharanya-ks19/realtime-telemetry-pipeline.git)
cd realtime-telemetry-pipeline
pip install fastapi uvicorn streamlit requests pandas
