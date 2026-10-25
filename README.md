# Pothole Detection Using YOLOv8

## Project Overview
This project detects potholes in road images using a YOLOv8 object
detection model trained on a labeled pothole dataset.

## Dataset
- Total images: 1,243
- Training images: 870
- Validation images: 248
- Test images: 125
- Classes: 1 (pothole)

The dataset itself is not included in this ZIP.

## Test Results
- Precision: 74.46%
- Recall: 57.31%
- mAP@50: 66.64%
- mAP@50-95: 34.83%

These results are from the held-out test split. Performance on new
roads and real-world images may differ.

## Model
YOLOv8n, with the best trained weights saved as `models/best.pt`.

## Run a Prediction
Install the required package:

    pip install ultralytics

From the project root, run:

    python src/predict.py --source path/to/road_image.jpg

Optional confidence threshold:

    python src/predict.py --source path/to/road_image.jpg --conf 0.25

## Project Contents
- models/best.pt: trained model weights
- src/predict.py: inference script
- results/test_metrics.json: test metrics
- results/sample_predictions/: example annotated predictions
- data.yaml: dataset configuration
- README.md: project documentation

## Limitations
The model can miss potholes or produce false detections. Its performance
has not been independently verified on unseen real-world road locations.
