import logging
import os

from api import send_request

DATA_PATH = 'data'
PREDICTIONS_PATH = 'data/results.csv'
SERVICE_LOGS_PATH = 'data/service_logs.log'
MODEL_PATH = 'model/deberta-v3-base-finetuned.onnx'
TOKENIZER_PATH = 'model/deberta-v3-base-finetuned'
TFIDF_TRAIN_DATASET_PATH = 'datasets/tfidf_train_essays.csv'


class Service:
    def __init__(self):
        """
            Инициализация сервиса.
        """
        os.makedirs(DATA_PATH, exist_ok=True)

        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler(SERVICE_LOGS_PATH)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        self.logger = logger
        self.message = None

    def get_answer(self):
        self.message = send_request()

    def print_message_in_tg(self):
        print(self.message)
        self.message = None


service = Service()
