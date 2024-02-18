
#entrainement : Entraîne YOLOv8n sur l'ensemble de données COCO128 pendant 100 époques à une taille d'image de 640. Pour une liste complète des arguments disponibles, voir la page Configuration.
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='coco128.yaml', epochs=100, imgsz=640)

"""
#validationb : Valide la précision du modèle YOLOv8n entraîné sur le jeu de données COCO128. Aucun argument n'a besoin d'être passé en tant que model conserve sa formation data et les arguments en tant qu'attributs du modèle.
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('path/to/best.pt')  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category
"""
"""
#prédiction : Utilise un modèle YOLOv8n entraîné pour faire des prédictions sur les images.
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image
"""

"""
#exporte : Exporte un modèle YOLOv8n vers un format différent comme ONNX, CoreML, etc.
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('path/to/best.pt')  # load a custom trained model

# Export the model
model.export(format='onnx')
"""