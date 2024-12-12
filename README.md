
# Flipkart_grid_6.0

# Hexagone
**Demo Video Link:** https://youtu.be/8s3sAIvPJv0?feature=shared


![Hexagone](photos/Website_Home)


**Step-by-Step Guide to Setting Up and Running the Application**

1. **Clone the Repository**
   ```bash
   https://github.com/gourab9817/Flipkart_grid_6.0.git
   ```
2. **Create a Virtual Environment**
    ```bash
   python -m venv Grid
   ```
3. **Activate the Virtual Environment**

   - **On Windows:**
     ```bash
     Grid\Scripts\activate
     ```
   - **On Linux/macOS:**
     ```bash
     source Grid/bin/activate
     ```
4. **Install Required Packages**
    ```bash
   pip install -r requirements.txt
    ```
5. **Run the Application**
 
   ```bash
   python manage.py runserver
   ```
   
### Freshness Detector

![Hexagone](/static/images/freshness-detector-img.png)
 - Predicts the freshness and identifies the class (type) of fruits and vegetables.
 - Utilizes a model I trained using a dataset from Kaggle with MobileNetV2 as the base model in TensorFlow.

### Feature Extractor

![Hexagone](/static/images/feature-extractor-img.png)
 - Extracts product details such as MRP, EAN, manufacture date, and expiry date using OCR powered by Pytesseract.
 - Processes the text to validate the expiry date of the product.


### Object Detection

![Hexagone](/static/images/object-detection-img.png)
 - Counts and highlights products within an image.
 - Employs the EfficientDet model from TensorFlow Hub.


### Dataset For `Freshness Detector`

**Download the dataset from Kaggle.**

- Link : https://www.kaggle.com/datasets/muhriddinmuxiddinov/fruits-and-vegetables-dataset

This dataset contains images of the following fruits and vegetables items:

**Fresh fruits-** fresh banana, fresh apple, fresh orange, fresh mango and fresh strawberry.

**Rotten fruits-** rotten banana, rotten apple, rotten orange, rotten mango and rotten strawberry.

**Fresh vegetables-** fresh potato, fresh cucumber, fresh carrot, fresh tomato and fresh bell pepper.

**Rotten vegetables-** rotten potato, rotten cucumber, rotten carrot, rotten tomato and rotten bell pepper.



### Pre-trained Model / Architecture for `Object Detection`

- Link : https://tfhub.dev/tensorflow/efficientdet/d0/1

### Tesseract OCR Engine for Optical Character Recognition

- Tesseract : https://github.com/tesseract-ocr/tesseract

- Pytesseract : https://pypi.org/project/pytesseract/


![Hexagone](/static/images/smart-vision-bottom.png)



