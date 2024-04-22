import os
import numpy as np
import SimpleITK as sitk
from tensorflow.keras.models import load_model # type: ignore
def load_nii_gz_files(folder_path):
    #* 从文件夹加载所有nii.gz文件并返回 numpy 数组列表
    file_names = sorted([f for f in os.listdir(folder_path) if f.endswith('.nii.gz')])
    images = []
    for file in file_names:
        print(f"Loading {file}...")
        try:
            image = sitk.GetArrayFromImage(sitk.ReadImage(os.path.join(folder_path, file)))
            images.append(image)
        except Exception as e:
            print(f"Error loading {file}: {e}")
    return images

def resize_slice_sitk(image_array, target_width, target_height):
    #* 将单个切片的大小调整为指定的宽度和高度
    image_sitk = sitk.GetImageFromArray(image_array)  # 将 numpy 数组转换为 SimpleITK 镜像
    resample_filter = sitk.ResampleImageFilter()
    original_size = image_sitk.GetSize()
    original_spacing = image_sitk.GetSpacing()

    # 计算新间距，仅考虑 x 和 y 方向
    new_spacing = [original_spacing[0] * (original_size[0] / target_width), 
                   original_spacing[1] * (original_size[1] / target_height)]

    # 对于 2D 图像处理，仅设置 x 和 y 大小和间距
    resample_filter.SetOutputSpacing(new_spacing + [original_spacing[-1]])  # 附加 z 轴间距以实现兼容性
    resample_filter.SetSize([target_width, target_height, 1])  # 深度（z 轴）设置为 1
    resample_filter.SetInterpolator(sitk.sitkLinear)
    
    # 执行重采样
    resized_slice = resample_filter.Execute(image_sitk)
    
    return sitk.GetArrayFromImage(resized_slice)  # 将 SimpleITK 图像转换回 numpy 数组