from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   #data='C:/Users/Utilisateur/Documents/GitHub/projet_M1/datasets/ia_yolo_detection/project2.v3i.yolov8/data.yaml',
   data='ia_yolo_detection/dataset_poussin/data.yaml',
   imgsz=640,
   epochs=5,
   batch=8,
   name='yolov8n_custom')

print("finis")
"""from ultralytics import YOLO

# Load a model
model = YOLO('ia_yolo_detection/project2.v3i.yolov8/yolov8n.yaml')  # build a new model from YAML

# Train the model
results = model.train(data='coco128.yaml', epochs=25, imgsz=640)
"""

"""
from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='custom_data.yaml',
   imgsz=640,
   epochs=10,
   batch=8,
   name='yolov8n_custom'"""