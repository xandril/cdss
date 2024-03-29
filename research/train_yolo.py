from ultralytics import YOLO

yolo_config = {'save_period': 10,
               'project': '../experiments/yolo8n_0_3_5_6_7',
               'name': 'try',
               'seed': 42,
               'epochs': 100,
               'imgsz': 512,
               # 'optimizer': 'AdamW',
               'data': '../data/vinbigdata_0_3_5_6_7/data.yml',
               'pretrained': True,
               'device': 0,
               'batch': 64,
               'patience': 5,
               'plots': True,
               'workers': 2,
               }
if __name__ == '__main__':
    model = YOLO('../experiments/yolo8n_5_6_7/try/weights/best.pt')

    # Display model information (optional)
    model.info()

    results = model.val()
    print(results)
