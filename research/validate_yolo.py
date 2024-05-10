from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('../experiments/yolo9с_0_1_3/try/weights/best.pt')
    model.info()

    results = model.val()
    print(results)
