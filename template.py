import os 

# Getting the file Names

folder_name = [
    "data/raw",  # Raw Hand LandMark Data
    "data/processed", # Processed Landmark Data
    "models", # Trained ML Models
    "src",  # The Source Code
    "notebook" # Jupyter NoteBook for Exprimwent 
]

file_names = [
    "data/__init__.py",
    "models/__init__.py",
    "src/hand_tracking.py",
    "src/collect_data.py",
    "src/train_model.py",
    "src/__init__.py",
    "src/recognize_gesture.py",
    "src_appplication_control.py",
    "src/main.py",
    "requirements.txt"
]

for folder in folder_name:
    os.makedirs(folder , exist_ok= True)

for file in file_names:
    with open(file , "w") as f:
        pass  # Creates an emplty file 

print("Folder Structure Made Succesfully")