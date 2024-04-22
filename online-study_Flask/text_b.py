import os
import numpy as np
import SimpleITK as sitk
from keras.models import load_model

from text_a import load_nii_gz_files, resize_slice_sitk # type: ignore
# 加载预训练模型
model = load_model('E:/unet_liver_segmentation.h5')

# 加载验证数据集
image_folder = '../liver_tumor_segmentation/test/imagesTr'
label_folder = '../liver_tumor_segmentation/test/labelsTr'
x_val_images = load_nii_gz_files(image_folder)
y_val_images = load_nii_gz_files(label_folder)

# 假设所有图像的大小都调整为统一大小
target_width, target_height = 512, 512  # 根据模型的预期输入形状调整目标大小

x_val_processed = [resize_slice_sitk(img[int(img.shape[0] / 2)], target_width, target_height) for img in x_val_images]
y_val_processed = [resize_slice_sitk(lbl[int(lbl.shape[0] / 2)], target_width, target_height) for lbl in y_val_images]

x_val = np.array(x_val_processed)[..., np.newaxis] / 255.0
y_val = np.array(y_val_processed)[..., np.newaxis]

# 在验证数据集上进行预测
predictions = model.predict(x_val)

# 使用 0.5 作为阈值将预测概率转换为二进制图像
predictions_binary = (predictions > 0.5).astype(np.uint8)

def dice_coefficient(true_mask, pred_mask):
    """Calculate the Dice coefficient."""
    intersection = np.sum(true_mask * pred_mask)
    sum_ = np.sum(true_mask) + np.sum(pred_mask)
    return 2.0 * intersection / sum_ if sum_ != 0 else 1.0

# 计算骰子系数
dice_scores = [dice_coefficient(true.squeeze(), pred.squeeze()) for true, pred in zip(y_val, predictions_binary)]
mean_dice = np.mean(dice_scores)
print(f"Mean Dice Coefficient: {mean_dice}")
#! dice 重合度