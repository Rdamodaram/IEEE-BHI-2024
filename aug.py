import os
import cv2
import albumentations as A

# Bypass SSL certificate verification for Albumentations
os.environ['CHECK_VERSION'] = '0'

# Define the augmentation pipeline
augmentation_pipeline = A.Compose([
    A.Rotate(limit=30, p=0.5),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
])

# Define the directory containing malignant images
malignant_dir = "/Users/rkoppula/IEEE/malignant"

# Define the directory where augmented images will be saved
augmented_dir = "/Users/rkoppula/IEEE/augmented"

# Apply augmentation to each malignant image
for filename in os.listdir(malignant_dir):
    image_path = os.path.join(malignant_dir, filename)
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if the image is loaded successfully
    if image is None:
        print(f'Failed to load image: {image_path}')
        continue
    
    # Apply augmentation
    augmented = augmentation_pipeline(image=image)
    augmented_image = augmented['image']
    
    # Save the augmented image
    augmented_filename = os.path.join(augmented_dir, f'augmented_{filename}')
    
    try:
        # Convert augmented image to BGR format
        augmented_image_bgr = cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR)
        
        # Convert image to uint8 before saving
        augmented_image_uint8 = (augmented_image_bgr * 255).astype('uint8')
        
        # Save the image
        cv2.imwrite(augmented_filename, augmented_image_uint8)
        print(f'Augmented image saved: {augmented_filename}')
    except Exception as e:
        print(f'Error saving augmented image: {e}')
