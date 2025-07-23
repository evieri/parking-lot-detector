from ultralytics import YOLO
import os

# 📁 Caminhos do projeto
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(PROJECT_PATH, "dataset")
YAML_PATH = os.path.join(DATASET_PATH, "data.yaml")
RESULTS_PATH = os.path.join(PROJECT_PATH, "results")

# ✅ Verifica se o YAML existe
if not os.path.exists(YAML_PATH):
    raise FileNotFoundError(f"❌ Arquivo data.yaml não encontrado em: {YAML_PATH}")

# 🧠 Treinar com YOLOv8 nano
model = YOLO("yolov8n.pt")  # Modelo pré-treinado

model.train(
    data=YAML_PATH,
    epochs=15,
    imgsz=640,
    project=RESULTS_PATH,
    name="yolov8n_results",
    exist_ok=True,
    device="cpu",  # Use "cuda" se quiser usar GPU
)
