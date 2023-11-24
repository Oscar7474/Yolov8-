from ultralytics import YOLO
if __name__ == "__main__":
  model = YOLO("yolov8n.yaml")#yolov8"n" can be replaced with "s" "m" "l" "x"
  results = model.train(
      data = "/Users/oscarkuo/Downloads/c.yaml" #It would be better to put an absolute path
  )
