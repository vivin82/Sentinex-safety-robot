# %%
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor driver 1 pins
IN1 = 17  # Input 1
IN2 = 27  # Input 2
IN3 = 22  # Input 3
IN4 = 23  # Input 4

# Motor driver 2 pins
IN5 = 5   # Input 5
IN6 = 6   # Input 6
IN7 = 13  # Input 7
IN8 = 19  # Input 8

# Set up all pins as outputs
motor_pins = [IN1, IN2, IN3, IN4, IN5, IN6, IN7, IN8]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Functions to control motors
def move_forward():
    # Motor driver 1
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    # Motor driver 2
    GPIO.output(IN5, GPIO.HIGH)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.HIGH)
    GPIO.output(IN8, GPIO.LOW)

def move_backward():
    # Motor driver 1
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    # Motor driver 2
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.HIGH)

def turn_left():
    # Motor driver 1
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    # Motor driver 2
    GPIO.output(IN5, GPIO.LOW)
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.HIGH)
    GPIO.output(IN8, GPIO.LOW)

def turn_right():
    # Motor driver 1
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    # Motor driver 2
    GPIO.output(IN5, GPIO.HIGH)
    GPIO.output(IN6, GPIO.LOW)
    GPIO.output(IN7, GPIO.LOW)
    GPIO.output(IN8, GPIO.HIGH)

def stop():
    # Stop all motors
    for pin in motor_pins:
        GPIO.output(pin, GPIO.LOW)

# Main function to test the motors
try:
    while True:
        command = input("Enter command (w: forward, s: backward, a: left, d: right, x: stop): ").lower()

        if command == "w":
            print("Moving forward")
            move_forward()
        elif command == "s":
            print("Moving backward")
            move_backward()
        elif command == "a":
            print("Turning left")
            turn_left()
        elif command == "d":
            print("Turning right")
            turn_right()
        elif command == "x":
            print("Stopping")
            stop()
        else:
            print("Invalid command")

        time.sleep(1)
        stop()  # Ensure the motors stop after each command

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    GPIO.cleanup()  # Reset GPIO settings


# %%
!git clone https://github.com/ultralytics/yolov5.git


# %%
!ls /content

# %%
import kagglehub

# Download latest version
path = kagglehub.dataset_download("snehilsanyal/construction-site-safety-image-dataset-roboflow")

print("Path to dataset files:", path)

# %%
!git clone https://github.com/ultralytics/yolov5.git /content/drive/MyDrive/yolov5


# %%
!git clone https://github.com/ultralytics/yolov5.git

# %%
!pip install ultralytics

# %%
%cd yolov5

# %%
!pip install -r requirements.txt

# %%
import torch

# %%
print("GPU available:", torch.cuda.is_available())


# %%
!python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images


# %%
from ultralytics import YOLO

# %%
# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# %%
from google.colab import files
uploaded = files.upload()

# %%
import zipfile

# Replace 'your_file.zip' with the uploaded ZIP file name
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/data')
print("Files extracted to /content/data")

# Use extracted files
data_dir = '/content/data'


# %%
zip_file_path = '/content/data'


# %%
import os

# List files in the current directory
print(os.listdir())
# Use the file name as the path
zip_file_path = '/content/data'



# %%
import zipfile
import os
import io

# Access the uploaded file from the 'uploaded' dictionary
zip_file_data = uploaded['archive.zip']

# Create an in-memory file-like object
zip_file = io.BytesIO(zip_file_data)

# Extract the ZIP file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall('/content/extracted')  # Extract contents to a directory

# List the extracted files
print(os.listdir('/content/extracted'))

# %%
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Assuming images are in subfolders of /content/data
datagen = ImageDataGenerator(rescale=1./255)
train_data = datagen.flow_from_directory(
    '/content/data',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# Model training (example)
from tensorflow.keras import models, layers

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_data, epochs=5)


# %%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a simple model
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# %%
from tensorflow.keras.models import load_model

# Load a pre-trained model
model = load_model('hgv.keras')


# %%
model.save('hgv.keras')

# Download the model
from google.colab import files
files.download('hgv.keras')


# %%
model.summary()


# %%
# Assuming you have training data and validation data
# Load or create your test data here
# Example:
import numpy as np  # Import numpy for creating sample data

# Replace these with your actual test data loading
x_test = np.random.rand(100, 10)  # Example: 100 samples with 10 features
y_test = np.random.randint(0, 2, size=100)  # Example: 100 binary labels (0 or 1)

model.evaluate(x_test, y_test)  # For evaluating the model on the test set

# %%
predictions = model.predict(x_test)  # or x_input for custom input
print(predictions)  # Check the predictions to see if they make sense


# %%
# Assuming you have training data and validation data
# Load or create your test data here
# Example:
import numpy as np  # Import numpy for creating sample data

# Replace these with your actual test data loading
num_samples = 1000  # Adjust as needed
num_features = 10  # Adjust as needed

# Create random training data
x_train = np.random.rand(num_samples, num_features)
y_train = np.random.randint(0, 2, size=num_samples)

# Create random validation data
x_val = np.random.rand(int(num_samples * 0.2), num_features)  # 20% for validation
y_val = np.random.randint(0, 2, size=int(num_samples * 0.2))


history = model.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val))

# You can then plot the training/validation loss/accuracy over epochs to check if the model is learning
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Val'])
plt.show()

# %%
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix # Import the confusion_matrix function

# Assuming you have your true labels (y_true) and predicted labels (y_pred)
# Replace these with your actual data:
y_true = [0, 1, 0, 1, 1, 0, 0, 1]  # Example true labels
y_pred = [1, 1, 0, 1, 0, 0, 1, 1]  # Example predicted labels

# Calculate the confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Plot confusion matrix using seaborn heatmap
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# %%
weights = model.get_weights()
print(weights)  # This will print out the model's weights for each layer


# %%
import cv2
import numpy as np
from tensorflow.keras.models import load_model  # If you have a pre-trained model

# Load your pre-trained model
model = load_model('hgv.keras')  # Or use model.save('model.h5') to load

# Open a video feed (0 for default webcam)
cap = cv2.VideoCapture(0)  # Use 'video_file.mp4' for video file input

def preprocess_frame(frame):
    # Resize frame to match the model's input size (assuming the model needs 224x224 input)
    frame_resized = cv2.resize(frame, (224, 224))

    # Normalize if required (e.g., if model expects values between 0 and 1)
    frame_normalized = frame_resized.astype('float32') / 255.0

    # Add batch dimension to match input shape (1, 224, 224, 3)
    frame_batch = np.expand_dims(frame_normalized, axis=0)
    return frame_batch

while True:
    # Read the next frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for prediction
    preprocessed_frame = preprocess_frame(frame)

    # Predict the class or objects from the frame
    prediction = model.predict(preprocessed_frame)

    # Process the prediction (you can modify based on what your model outputs)
    # For classification: Convert the prediction to a class label
    predicted_class = np.argmax(prediction, axis=1)  # for classification
    predicted_confidence = np.max(prediction)  # Get the confidence score

    # Display the prediction on the video frame
    label = f"Class: {predicted_class[0]}, Confidence: {predicted_confidence:.2f}"
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # --- Code added from ipython-input-86-c7969011ca62 ---
    # Example for object detection (if needed)
    # Assuming 'prediction' gives bounding boxes, class ids, and confidences
    # Modify this part based on your model's prediction output:
    # Assuming prediction is a list with [boxes, class_ids, confidences]

    # IF prediction is NOT in the expected format, print it out for debugging:
    # print("Prediction:", prediction)
    # print("Prediction Shape:", prediction.shape) # If prediction is a NumPy array

    if isinstance(prediction, (list, tuple)) and len(prediction) >= 3:
        for box, class_id, confidence in zip(prediction[0], prediction[1], prediction[2]):
            # Draw bounding box on the frame
            x, y, w, h = box  # Assuming box is in (x, y, width, height) format
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Class: {class_id}, Conf: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    # --- End of added code ---


    # Display the frame with the prediction
    cv2.imshow('Video Feed with Predictions', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# %%
 import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('hgv.keras')  # Update with your model path
# Open a video feed (0 for default webcam)
cap = cv2.VideoCapture(0)  # Use 'video_file.mp4' for a video file
def preprocess_frame(frame):
    # Resize the frame to match the model's expected input (e.g., 224x224x3)
    frame_resized = cv2.resize(frame, (224, 224))

    # Normalize if required (e.g., if model expects values between 0 and 1)
    frame_normalized = frame_resized.astype('float32') / 255.0

    # Add batch dimension to match input shape (1, 224, 224, 3)
    frame_batch = np.expand_dims(frame_normalized, axis=0)
    return frame_batch
while True:
    # Read a frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for prediction
    preprocessed_frame = preprocess_frame(frame)

    # Make the prediction (e.g., classifying if safety gear is present)
    prediction = model.predict(preprocessed_frame)

    # Assuming the model outputs probabilities, classify the result
    predicted_class = np.argmax(prediction, axis=1)
    class_names = ['No Gear', 'Helmet', 'Gloves', 'Safety Vest']  # Example classes
    predicted_label = class_names[predicted_class[0]]

    # Display the label on the frame
    cv2.putText(frame, f"Safety Gear: {predicted_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with the prediction
    cv2.imshow('Safety Gear Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for the detection model
    preprocessed_frame = preprocess_frame(frame)

    # Make the prediction (this might include bounding boxes, class IDs, and confidences)
    prediction = model.predict(preprocessed_frame)

    # Example: Assume prediction contains bounding boxes and class IDs for detected safety gear
    # Loop over detected objects and draw bounding boxes
    for i in range(prediction.shape[0]):  # Loop through each detected object
        class_id = np.argmax(prediction[i][:-1])  # Class ID (assume last element is confidence)
        confidence = prediction[i][-1]  # Confidence score
        if confidence > 0.5:  # Set a threshold for confidence

            # Get the bounding box coordinates
            x, y, w, h = prediction[i][:4]

            # Draw the bounding box
            cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)

            # Add label for the object
            label = f"Class: {class_id}, Conf: {confidence:.2f}"
            cv2.putText(frame, label, (int(x), int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with the detected safety gear
    cv2.imshow('Safety Gear Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()
# Open the video file
cap = cv2.VideoCapture('your_video_file.mp4')




# %%
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load your pre-trained model
model = load_model('hgv.keras')  # Update path to your model file

# Open a video feed (default webcam)
cap = cv2.VideoCapture(0)

# Optional: Define video writer for saving output video
frame_width = int(cap.get(3))  # Width of the video frames
frame_height = int(cap.get(4))  # Height of the video frames
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))

def preprocess_frame(frame):
    """
    Preprocess the input frame to match the model's input size.
    """
    # Resize frame to match the model's input size
    frame_resized = cv2.resize(frame, (224, 224))  # Adjust size if required by your model
    # Normalize pixel values to [0, 1]
    frame_normalized = frame_resized.astype('float32') / 255.0
    # Add batch dimension
    frame_batch = np.expand_dims(frame_normalized, axis=0)
    return frame_batch

while cap.isOpened():
    # Capture each frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Preprocess the frame
    preprocessed_frame = preprocess_frame(frame)

    # Get predictions from the model
    prediction = model.predict(preprocessed_frame)

    # Interpret the model's output
    predicted_class = np.argmax(prediction, axis=1)[0]  # For classification models
    predicted_confidence = np.max(prediction)  # Get the confidence score

    # Add predictions to the frame
    label = f"Class: {predicted_class}, Confidence: {predicted_confidence:.2f}"
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Live Feed with Predictions', frame)

    # Save the frame to a video file (optional)
    output.write(frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
output.release()  # Release video writer
cv2.destroyAllWindows()


# %%



