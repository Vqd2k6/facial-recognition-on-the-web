# Nhận diện khuôn mặt trên web

## Giới thiệu

Đây là dự án về nhận diện khuôn mặt trên nền tảng web. Ứng dụng sử dụng các công nghệ về machine learning và xử lý ảnh để nhận diện khuôn mặt từ ảnh hoặc webcam trực tiếp. Dự án phù hợp để áp dụng vào các hệ thống xác thực, điểm danh, hoặc nâng cao trải nghiệm người dùng cho các ứng dụng web.

## Tính năng nổi bật

- Nhận diện khuôn mặt từ ảnh tải lên hoặc qua webcam
- Phân tích và trích xuất đặc trưng khuôn mặt
- So sánh và xác thực khuôn mặt
- Giao diện người dùng đơn giản, thân thiện

## 🛠️ Công Nghệ Sử Dụng

| Thành phần       | Công nghệ                | Chi tiết                                         |
|:-----------------|:------------------------|:-------------------------------------------------|
| **Backend**      | Python                  | FastAPI, Uvicorn                                 |
| **AI Engine**    | InsightFace             | Model Buffalo_L, ONNX Runtime                    |
| **Xử lý ảnh**    | OpenCV, NumPy           | Xử lý ma trận ảnh và vector                      |
| **Frontend**     | HTML5, CSS3             | Giao diện tùy chỉnh (Custom UI)                  |
| **Client Script**| JavaScript              | Face-API.js (TensorFlow.js core)                 |
| **Database**     | JSON                    | Lưu trữ đơn giản (File-based)                    |

## Hướng dẫn cài đặt

1. **Clone source code:**
   ```bash
   git clone https://github.com/Vqd2k6/facial-recognition-on-the-web.git
   ```

## 🧩 Hướng Dẫn Cài Đặt Thư Viện

Dự án sử dụng các thư viện Python sau:

- `fastapi`
- `uvicorn`
- `pydantic-settings`
- `insightface`
- `onnxruntime` <br>Hoặc `onnxruntime-gpu` nếu bạn có card NVIDIA hỗ trợ CUDA
- `opencv-python-headless`
- `python-multipart`
- `jinja2`
- `numpy`

Để cài đặt tất cả thư viện trên, bạn hãy chạy lệnh sau trong terminal tại thư mục dự án:

```bash
pip install fastapi uvicorn pydantic-settings insightface onnxruntime opencv-python-headless python-multipart jinja2 numpy
```

**Lưu ý:**
- Nếu máy bạn có card đồ họa NVIDIA và muốn sử dụng GPU, thay thế `onnxruntime` bằng `onnxruntime-gpu`:
  ```bash
  pip install onnxruntime-gpu
  ```
- Khuyến khích sử dụng môi trường ảo (virtualenv) để tránh xung đột thư viện với các dự án khác:
  ```bash
  python -m venv venv
  source venv/bin/activate # hoặc venv\Scripts\activate trên Windows
  ```

Sau khi hoàn tất cài đặt, bạn có thể khởi động và sử dụng dự án theo hướng dẫn ở trên.

## ▶️ Cách Chạy Dự Án

Để khởi động server, mở terminal tại thư mục gốc và chạy lệnh sau:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Sau khi khởi động thành công, truy cập trình duyệt tại địa chỉ:  
👉 [http://localhost:8000](http://localhost:8000)

## Đóng góp dự án

Chào mừng mọi đóng góp về code, tài liệu, ý tưởng hoặc báo lỗi! Vui lòng tạo Pull Request hoặc Issue mới trên Github.

## Tác giả

- Vqd2k6 ([github.com/Vqd2k6](https://github.com/Vqd2k6))

## Giấy phép

Dự án này được phát hành theo giấy phép MIT.
