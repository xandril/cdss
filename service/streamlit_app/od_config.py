MIN_CONFIDENCE_THRESHOLD = 0.0
MAX_CONFIDENCE_THRESHOLD = 1.0
DEFAULT_CONFIDENCE_THRESHOLD = 0.3

DEFAULT_CLASSES_TO_INCLUDE = [
    "Aortic enlargement",
    "Atelectasis",
    # "Calcification",
    "Cardiomegaly",
    # "Consolidation",
    "ILD",
    "Infiltration",
    "Lung Opacity",
    # "Nodule/Mass",
    # "Pleural effusion",
    # "Pleural thickening",
    # "Pneumothorax",
    # "Pulmonary fibrosis"
]

# Assign colors to each label
CLASS_COLOURS = [
    "red",
    "green",
    "blue",
    "purple",
    "orange",
    "cyan",
    # "magenta",
    # "yellow",
    # "pink",
    # "brown",
    # "lime",
    # "teal",
    # "olive"
]
CLASS_COLOUR_DICT = dict(zip(DEFAULT_CLASSES_TO_INCLUDE, CLASS_COLOURS))

API_ENDPOINT = 'http://127.0.0.1:4242/detect_objects'
