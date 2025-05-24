# smoking-task
# Smoking Detection

基于 YOLO 模型的吸烟行为检测系统，支持图片、视频和实时摄像头推理。

## 项目功能

- 📷 支持图片推理
- 🎞 支持视频推理（.mp4/.mov）
- 📹 实时摄像头推理
- ✅ 自动保存检测结果

## 使用方法

### 1. 安装依赖

```bash
pip install -r requirements.txt
```
### 2.开始推理

####图片推理
python detect.py --source <图片路径>

####视频推理
python detect.py --source <视频路径>

####实时监控推理
python detect.py --source 0
```

