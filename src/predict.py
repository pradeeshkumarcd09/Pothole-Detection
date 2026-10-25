from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser(description="Pothole detection")
parser.add_argument("--source", required=True,
                    help="Path to an image, video, or image folder")
parser.add_argument("--conf", type=float, default=0.25,
                    help="Detection confidence threshold")
args = parser.parse_args()

model = YOLO("models/best.pt")
model.predict(
    source=args.source,
    conf=args.conf,
    imgsz=640,
    save=True
)
