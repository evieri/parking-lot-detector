
# 🚗 Detector de Ocupação Indevida em Vagas de Estacionamento

Este projeto utiliza **YOLOv8** e **Visão Computacional** para detectar automaticamente vagas de estacionamento ocupadas ou livres em imagens de estacionamentos.

![Exemplo da Inferência](images/exemplo_inferencia.jpg)

---

## 📁 Estrutura do Projeto

```

partking-lot-detector/
│
├── data/                 # Dataset convertido para YOLO
├── runs/                 # Resultados de treinamento
├── inference.py          # Script de inferência com Gradio
├── train.py              # Script de treino do YOLOv8
├── README.md             # Este arquivo
└── requirements.txt      # Dependências

````

---

## 🚀 Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/partking-lot-detector.git
cd partking-lot-detector
````

### 2. Instale as Dependências

Você pode usar um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

### 3. Execute a Inferência

Rode a interface do Gradio para testar o modelo localmente:

```bash
python inference.py
```

Isso abrirá uma interface no navegador para você carregar imagens.

---

## 🏋️ Treinamento do Modelo

O treinamento foi realizado com o modelo `YOLOv8s` por 15 épocas com um subconjunto do dataset.

Para treinar novamente:

```bash
yolo task=detect mode=train model=yolov8s.pt data=data.yaml epochs=15
```

> Requer [Ultralytics](https://github.com/ultralytics/ultralytics) instalado e dataset formatado.

---

## 📊 Resultados

* **Precision:** 95.84%
* **Recall:** 96.28%
* **mAP\@0.5:** 97.77%
* **mAP\@0.5:0.95:** 71.80%

---

## 🧠 Tecnologias Utilizadas

* YOLOv8
* Gradio
* Python
* Roboflow
* Google Colab

---

## 📚 Referências

* [Dataset no Kaggle](https://www.kaggle.com/datasets)
* [YOLOv8 - Ultralytics](https://docs.ultralytics.com)
* [Roboflow](https://roboflow.com)
* [Gradio](https://www.gradio.app)

---

## 📸 Exemplos Visuais

* *(Inserir prints dos resultados de inferência e tela do Gradio na pasta `images/`)*

---

## ✨ Autor

Emmanuel Vieri Barros Lucas

