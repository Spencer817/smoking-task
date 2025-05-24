from ultralytics import YOLO
import cv2
import argparse
import sys
import os

# 创建保存目录
os.makedirs('runs', exist_ok=True)

# 解析命令行参数
parser = argparse.ArgumentParser(description='YOLO 吸烟检测')
parser.add_argument('--source', type=str, default='0', help='推理源，摄像头为0，视频或图片文件路径')
args = parser.parse_args()

# 加载吸烟检测模型
model = YOLO('best.onnx')  # 请确保 best.onnx 模型文件存在

source = args.source
ext = os.path.splitext(source)[1].lower()
image_exts = ['.jpg', '.jpeg', '.png']

# 判断是否为图片
if ext in image_exts:
    frame = cv2.imread(source)
    if frame is None:
        print(f"无法读取图片文件: {source}")
        sys.exit(1)
    results = model(frame)
    result = results[0]
    annotated_frame = result.plot()
    cv2.imshow('YOLO 吸烟检测', annotated_frame)
    cv2.imwrite('runs/annotated_output.jpg', annotated_frame)
    # 等待 ESC 退出
    while True:
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
else:
    # 视频/摄像头
    if source == '0' or source.isdigit():
        cap = cv2.VideoCapture(int(source))
    else:
        cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"无法打开推理源: {source}")
        sys.exit(1)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('runs/output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法获取摄像头画面。")
            break

        # 运行 YOLO 推理
        results = model(frame)
        result = results[0]

        # 绘制检测结果
        annotated_frame = result.plot()

        # 显示带注释的画面
        cv2.imshow('YOLO 吸烟检测', annotated_frame)

        # 保存帧到视频
        out.write(annotated_frame)

        # 按 ESC 退出
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()