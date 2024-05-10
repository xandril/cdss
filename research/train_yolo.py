from ultralytics import YOLO

yolo_config = {'save_period': 10,
               'project': '../experiments/yolo9с_0_1_3',
               'name': 'try',
               'seed': 42,
               'epochs': 50,
               'imgsz': 512,
               # 'optimizer': 'AdamW',
               'data': '../data/vinbigdata_0_1_3 /data.yml',
               'pretrained': True,
               'device': 0,
               'batch': 16,
               'patience': 5,
               'plots': True,
               'workers': 2,
               }
if __name__ == '__main__':
    # model = YOLO('../experiments/yolo8n_5_6_7/try/weights/best.pt')
    model = YOLO('../models/pretrained/yolo/yolov9c.pt')
    # Display model information (optional)
    model.info()

    results = model.train(**yolo_config)
    print(results)
    print(model.val())
