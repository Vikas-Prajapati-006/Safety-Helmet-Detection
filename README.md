# 🦺 Safety Helmet Detection System

An end-to-end AI engineering project designed for industrial safety compliance. This system utilizes the YOLOv8 architecture to detect whether personnel are wearing safety helmets in real-time.



## 🛠️ Technical Architecture
The project follows a modular programming approach, ensuring scalability and ease of maintenance.

*   **Model**: YOLOv8 (Ultralytics) for high-speed, single-shot object detection.
*   **Backend**: Flask-based web server for handling image inference requests.
*   **Pipeline**: Custom-built prediction pipeline in `src/pipeline/` for pre-processing and model inference.
*   **Infrastructure**: Fully containerized using **Docker** for consistent cross-environment deployment.
*   **MLOps**: Integrated custom logging and exception handling modules.

## 🏗️ Project Structure
* `src/`: Core source code (Data ingestion, Components, Pipelines).
* `templates/`: HTML interface for the web portal.
* `app.py`: The main entry point of the application.
* `best.pt`: Custom trained YOLOv8 model weights.
* `Dockerfile`: Containerization script for cloud deployment.
* `.dockerignore`: Optimization for fast and secure Docker builds.

## 📈 Impact
Ensures consistent monitoring of safety protocols in industrial zones, reducing human error in safety inspections.



