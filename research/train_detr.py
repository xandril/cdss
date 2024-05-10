from ultralytics import YOLO, RTDETR

yolo_config = {'save_period': 10,
               'project': '../experiments/detr_1',
               'name': 'try',
               'seed': 42,
               'epochs': 50,
               'imgsz': 512,
               'optimizer': 'AdamW',
               'data': '../data/vinbigdata_1/data.yml',
               'pretrained': True,
               'device': 0,
               'batch': 8,
               'patience': 5,
               'plots': True,
               'workers': 4,
               }
if __name__ == '__main__':
    model = RTDETR('rtdetr-l.pt')

    # Display model information (optional)
    model.info()

    results = model.train(**yolo_config)

    print(model.val())
