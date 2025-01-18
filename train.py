import os

os.environ['WANDB_DISABLED'] = 'true'
from ultralytics import YOLO
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", str, default="snn_yolov11l.yaml")
    # model =YOLO("snn_yolov8l.yaml").load('69M_best.pt')
    model =YOLO(parser.config)
    print(model)

    #train
    # model.train(data="coco.yaml",device=[7],epochs=100)  # train the model
    model.train(data="coco.yaml",device=[0,1,2,3],epochs=100)  # train the model

    #TEST
    # model = YOLO('runs/detect/train1/weights/last.pt')  # load a pretrained model (recommended for training)

