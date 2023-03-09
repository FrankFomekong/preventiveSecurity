# YOLOFace

# Deep learning based Face detection using the YOLOv3 algorithm

## NB this repo  [link](https://github.com/FrankFomekong/preventiveSecurity/) have two branc master and rest-api every everyone have his own README
## Getting started

The YOLOv3 (You Only Look Once) is a state-of-the-art, real-time object detection algorithm. The published model recognizes 80 different objects in images and videos
## YOLOv3's architecture

![Imgur](assets/yolo-architecture.png)

## OpenCV Deep Neural Networks (dnn module)

OpenCV `dnn` module supports running inference on pre-trained deep learning models from popular frameworks such as TensorFlow, Torch, Darknet and Caffe.

## Prerequisites

* Tensorflow
* opencv-python
* opencv-contrib-python
* Numpy
* Keras
* Matplotlib
* Pillow

Development for this project will be isolated in Python virtual environment. This allows us to experiment with different versions of dependencies.

There are many ways to install `virtual environment (virtualenv)`, see the [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/) guide for different platforms, but here are a couple:

- For Ubuntu
```bash
$ pip install virtualenv
```

- For windows
```cmd
$ pip install --upgrade virtualenv
```

Create a Python >= 3.6 virtual environment for this project and activate the virtualenv:
```bash
$ virtualenv -p python3.X yoloface
$ source ./yoloface/bin/activate
```

Next, install the dependencies for the this project:
```bash
$ pip install -r requirements.txt
```

## Usage

* Clone this repository
```bash
$ git clone https://github.com/FrankFomekong/preventiveSecurity/
```

* For face detection, you should download the pre-trained YOLOv3 weights file which trained on the [WIDER FACE: A Face Detection Benchmark](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/index.html) dataset from these [link](https://drive.google.com/file/d/1-36p9DWxwq-KP3uV9_hfrL1j-C6lk-qL/view?usp=sharing)  [for gpu](https://drive.google.com/file/d/1-EPjQs1s8wghjU8ufBc8eS0m54mYxdKs/view?usp=sharing) and place them in the `model-weights/` directory.

* Run the following command:

>**image input**
```bash
$ python yoloface.py --image samples/outside_000001.jpg --output-dir outputs/
```

>**video input**
```bash
$ python yoloface.py --video samples/subway.mp4 --output-dir outputs/
```

>**webcam**
```bash
$ python yoloface.py --src 1 --output-dir outputs/

note that you can replace '1' with the url of video stream 


