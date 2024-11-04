import slideio
import os
from pathlib import Path

def convert_vsi_to_svs(input_dir, output_dir):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 获取所有VSI文件
    vsi_files = list(Path(input_dir).glob("*.vsi"))
    
    # 设置转换参数
    params = slideio.SVSJpegParameters()
    params.quality = 70  # 压缩质量
    
    print(f"找到 {len(vsi_files)} 个VSI文件待转换...")
    
    # 遍历处理每个文件
    for vsi_path in vsi_files:
        try:
            # 构建输出文件路径
            output_path = os.path.join(output_dir, vsi_path.stem + ".svs")
            
            print(f"正在转换: {vsi_path.name}")
            
            # 打开并转换场景
            scene = slideio.open_slide(str(vsi_path), 'AUTO').get_scene(0)
            slideio.convert_scene(scene, params, output_path)
            
            print(f"转换完成: {output_path}")
            
        except Exception as e:
            print(f"转换 {vsi_path.name} 时出错: {str(e)}")
            continue

if __name__ == "__main__":
    # 设置输入输出路径
    input_directory = "./in"
    output_directory = "./out"
    
    # 执行转换
    convert_vsi_to_svs(input_directory, output_directory)
    print("所有转换已完成!")
