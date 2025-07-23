import gradio as gr
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import os

# 📁 Caminho do modelo
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(PROJECT_PATH, "results", "yolov8n_results", "weights", "best.pt")

# ✅ Verifica se o modelo existe
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Modelo não encontrado em: {MODEL_PATH}")

# 🔄 Carrega o modelo treinado
model = YOLO(MODEL_PATH)

def detectar_vagas(imagem):
    """Detecta vagas de estacionamento na imagem enviada"""
    if imagem is None:
        return None

    try:
        imagem_array = np.array(imagem)
        imagem_bgr = cv2.cvtColor(imagem_array, cv2.COLOR_RGB2BGR)
        resultados = model(imagem_bgr)
        imagem_anotada = resultados[0].plot()
        imagem_rgb = cv2.cvtColor(imagem_anotada, cv2.COLOR_BGR2RGB)
        return Image.fromarray(imagem_rgb)
    except Exception as e:
        print(f"Erro durante a inferência: {e}")
        return imagem

# 🎛️ Interface Gradio
demo = gr.Interface(
    fn=detectar_vagas,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="Detector de Ocupação de Vagas",
    description="Envie uma imagem de estacionamento. O modelo YOLOv8 detectará se as vagas estão livres ou ocupadas."
)

if __name__ == "__main__":
    demo.launch(debug=True)
