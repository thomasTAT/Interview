# ReadMe

# Abstract

The purpose of this report is to utilize deep learning to train a model for identifying dangerous motorcycle driving. First, YOLO is used to capture images and extract sections containing people and vehicles. Then, these images are fed into the model for training and prediction. Additionally, the Gradio framework is used to display the results. I am responsible for Method 1 in this project. Group 10 poster.jpg demonstrates this project.

## **Original yolo crop**

This program uses native YOLO to crop images taken with our phones, leaving only the parts with motorcycles and people.

Here's an example:https://www.kaggle.com/code/qaqthomas/original-yolo-corp-image/edit/run/180897458

To run this code, first import the `original-yolo-corp-image.ipynb` and [image](https://www.kaggle.com/datasets/qaqthomas/all-in-4-class-balance-onehand-2024-3-19) file to Kaggle.

Modify the path to the image file directory. The URL can be set to the path of a randomly selected image from the file for testing.

```
path ="/kaggle/input/all-in-4-class-balance-onehand-2024-3-19"
url = '/kaggle/input/all-in-4-class-balance-onehand-2024-3-19/01/IMG_20240110_121021.jpg'
```

Once the setup is complete, simply click "Save Version" to run the notebook, and the output results will be generated.

## Customize yoloV8 crop model

This program uses customize YOLO to crop images taken with our phones, leaving only the parts with motorcycles and people.

Here is an example: https://www.kaggle.com/code/qaqthomas/customize-yolov8-crop-model/edit/run/178888429

To run this code first, Import the `customize-yolov8-crop-model.ipynb` notebook to Kaggle. Then, upload our [images](https://www.kaggle.com/datasets/qaqthomas/all-in-4-class-balance-onehand-2024-3-19) and `yolo_crop_motorcycle_driver_model.pt` to Kaggle as well.

Next, set the YOLO path to the directory where you have stored the YOLO model. Here is an example.

```python
yolo = YOLO("/kaggle/input/yolo-motorcycle-driver/best.pt")
```

Then, set the paths for the input image folder and the output save directory. Here is an example.

```python
input_dir = '/kaggle/input/all-in-4-class-balance-onehand-2024-3-19'
output_dir1 = '/kaggle/working/image/'
```

Click "Save Version" to run the notebook and generate the results.

## Training light way CNN

This code is for training a light way CNN.

Here is an example: https://www.kaggle.com/code/qaqthomas/light-way-good-cnn/edit/run/178945312

- Import the `light-way-good-cnn.ipynb` notebook to Kaggle.
- Upload the folder of images cropped using YOLO.
- Set the correct image file path in the code. Here is an example.
    
    ```python
    x, y = load_images("/kaggle/input/all-in-4-class-after-yolo-crop-2024-3-19")
    ```
    
- Click "Save Version."
- The ligth way CNN model will be trained, and you will see the performance of this model. You will also save the model and the images from the test set that are predicted as dangerous driving.

## Training MobileNet

This code is for fine-tuning MobileNet.

Here is an example: https://www.kaggle.com/code/qaqthomas/mobilenet-train-only/edit/run/178924261

1. Import the `mobilenet-train-only.ipynb` notebook to Kaggle.
2. Upload the folder of images cropped using YOLO.
3. Set the correct image file path in the code. Here is an example.
    
    ```python
    x, y = load_images("/kaggle/input/all-in-4-class-after-yolo-crop-2024-3-19")
    ```
    
4. Click "Save Version."
5. The MobileNet model will be trained, and you will see the performance of this model. You will also save the model and the images from the test set that are predicted as dangerous driving.

## Yolo mobilenet gradio interface

此文檔,利用gradio,可視化 model prediction. 原理: 用戶上傳圖片, yolo corp -> mobilenet predict -> return result.

Here is an exmaple: https://colab.research.google.com/drive/1rFjFmX1c6D7EU-utGHPRGi9n6WBbtVaJ

1. Upload `yolo mobilenet gradio interface.ipynb` to [colab.research.google.com](https://colab.research.google.com/).
2. Upload the `mobilenet_model.keras` to Google Drive.
3. Set the correct path for the model in the notebook. Here is an example.
    
    ```python
    model = load_model("/content/drive/MyDrive/Colab Notebooks/model/best_model.keras")
    ```
    
4. Run the notebook to create a Gradio interface where you can drag and drop images for testing.