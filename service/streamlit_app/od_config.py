MIN_CONFIDENCE_THRESHOLD = 0.0
MAX_CONFIDENCE_THRESHOLD = 1.0
DEFAULT_CONFIDENCE_THRESHOLD = 0.3

DEFAULT_CLASSES_TO_INCLUDE = ['Cardiomegaly', 'Aortic enlargement', 'ILD', 'Infiltration', 'Lung Opacity']
CLASS_COLOURS = ["red", "green", "blue", "yellow", "cyan"]
CLASS_COLOUR_DICT = dict(zip(DEFAULT_CLASSES_TO_INCLUDE, CLASS_COLOURS))

API_ENDPOINT = 'http://127.0.0.1:4242/detect_objects'
