# SpikeYOLOv2: Advancing SpikeYOLO for Efficient and Robust Object Detection
## 🚀 Training
Run the following commands to train SpikeYOLOv2 on COCO 2017 dataset.
```bash
python train.py
```

## 💡 Inference
Run the following commands to test the performance of SpikeYOLOv2 on COCO 2017 dataset.
```bash
python test.py
```

## 📚 Ablation Study
Run the following commands to train the model with different configurations on COCO 2017 dataset.
### Classifier head
```bash
python train.py --config "snn_yolov11_head.yaml"
```
### SpikeC2PSA
```bash
python train.py --config "snn_yolov11_SpikeC2PSA.yaml"
```
### Test
Change the checkpoint path in `test.py` to the path of the trained model and run the following commands to test the performance of the models that only change classifier head or SpikeC2PSA module.
```bash
python test.py
```
## Thanks

Our implementation is mainly based on the following codebases. We gratefully thank the authors for their wonderful works.
https://github.com/BICLab/SpikeYOLO

https://github.com/ultralytics/ultralytics
