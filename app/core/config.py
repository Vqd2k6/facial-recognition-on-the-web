import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 1. Cấu hình chung
    PROJECT_NAME: str = "Face_Project"
    API_VERSION: str = "/api/v1"

    # 2. Cấu hình Database
    # Dùng đường dẫn tuyệt đối để tránh lỗi khi chạy ở thư mục khác
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DB_FILE: str = os.path.join(BASE_DIR, "users_db.json")

    # 3. Cấu hình AI & Model
    MODEL_DIR: str = os.path.join(BASE_DIR, "models")
    STATIC_DIR: str = os.path.join(BASE_DIR, "static")
    INSIGHTFACE_MODEL_NAME: str = "buffalo_l"
    AI_PROVIDER: list = ['CPUExecutionProvider']

    # Quan trọng:
    FACE_SIMILARITY_THRESHOLD: float = 0.9

    class Config:
        case_sensitive = True


# Khởi tạo biến settings để dùng ở các file khác
settings = Settings()