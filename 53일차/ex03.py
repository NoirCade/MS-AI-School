import cv2
import random
import albumentations as A


# Define function to visualize
def visualize(image):
    cv2.imshow('visualization', image)
    cv2.waitKey(0)

# Load image form drive
image = cv2.imread('./weather.png')

# visualize original
# visualize(image)

# RandomWeather
transform = A.Compose([
    # A.RandomRain(brightness_coefficient=0.8, drop_width=3, blur_value=5, p=1)
    # A.RandomSnow(brightness_coeff=2.0, snow_point_lower=0.1, snow_point_upper=0.3, p=1),
    # A.RandomSunFlare(flare_roi=(0, 0, 1, 0.5), angle_lower=0.3, p=1),
    # A.RandomShadow(num_shadows_lower=2, num_shadows_upper=2, shadow_dimension=5, shadow_roi=(0, 0.5, 1, 1), p=1),
    A.RandomFog(fog_coef_lower=0.3, fog_coef_upper=0.8, alpha_coef=0.08, p=1)
])


transformed = transform(image=image)
visualize(transformed['image'])
