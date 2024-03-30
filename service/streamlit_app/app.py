from dataclasses import dataclass

import requests
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

import od_config


def draw_boxes(raw_img_data,
               bboxes: list[dict[str, int]],
               scores: list[float],
               labels: list[str],
               settings_dict: dict[str]) -> Image.Image:
    img = Image.open(raw_img_data).convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', size=10)

    for bbox, score, label in zip(bboxes, scores, labels):
        if score <= settings_dict['model_confidence'] or label not in settings_dict['included_classes']:
            continue

        rect = (bbox['x0'], bbox['y0']), (bbox['x1'], bbox['y1'])
        color = od_config.CLASS_COLOUR_DICT[label]
        draw.rectangle(rect, outline=color, width=2)
        if settings_dict['show_classes']:
            label = f"{label} ({score:.2f})"
            draw.text((rect[0][0], rect[0][1] - 20), label, fill=color, font=font)
    return img


@dataclass
class DetectionResult:
    bboxes: list[dict[str, int]]
    scores: list[float]
    labels: list[str]


def detection_callback():
    try:
        response = requests.post(
            od_config.API_ENDPOINT,
            files={"file": uploaded_file},
        )
        response.raise_for_status()

        detection_data_dict = response.json()

        st.session_state.detection_data = DetectionResult(bboxes=detection_data_dict["bboxes"],
                                                          labels=detection_data_dict['labels'],
                                                          scores=detection_data_dict['scores'])

    except requests.exceptions.HTTPError as errh:
        st.error("Http Error:")
    except requests.exceptions.ConnectionError as errc:
        st.error("Error Connecting")
    except requests.exceptions.Timeout as errt:
        st.error("Timeout Error:")
    except requests.exceptions.RequestException as err:
        st.error("OOps: Something Else")
    # TODO MAKE NORMAL ERROR HANDLING


def clear_detection_data():
    st.session_state.detection_data = None


def init_sidebar() -> dict:
    with st.sidebar:
        st.header('Settings')
        model_conf = st.slider(label='model confidence threshold',
                               min_value=od_config.MIN_CONFIDENCE_THRESHOLD,
                               max_value=od_config.MAX_CONFIDENCE_THRESHOLD,
                               value=od_config.DEFAULT_CONFIDENCE_THRESHOLD)

        show_classes_radio = st.radio(label='show box labels',
                                      options=['yes', 'no'])

        included_classes = st.multiselect(label='choose classes to include',
                                          options=od_config.DEFAULT_CLASSES_TO_INCLUDE,
                                          default=od_config.DEFAULT_CLASSES_TO_INCLUDE)

        return {'model_confidence': model_conf,
                'show_classes': True if show_classes_radio == 'yes' else False,
                'included_classes': included_classes,
                }


def init_header():
    st.set_page_config(page_title="cdss od pipeline",
                       layout="wide")


if __name__ == '__main__':
    init_header()

    settings_dict = init_sidebar()
    if 'detection_data' not in st.session_state:
        st.session_state.detection_data = None

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], on_change=clear_detection_data)

    if uploaded_file is not None:
        if st.session_state.detection_data is None:
            st.button(label='make detection', on_click=detection_callback)
            st.image(uploaded_file, caption="Original Image", use_column_width=True)

        else:
            detection_data = st.session_state.detection_data
            processed_img = draw_boxes(raw_img_data=uploaded_file,
                                       bboxes=detection_data.bboxes,
                                       scores=detection_data.scores,
                                       labels=detection_data.labels,
                                       settings_dict=settings_dict)
            st.image([uploaded_file, processed_img],
                     caption=["Original Image", "Processed Image"], use_column_width=True)
