import insightface
import numpy as np
import cv2
import base64
from app.core.config import settings  # <--- Import settings


class AIEngine:
    def __init__(self):
        print(f"⏳ Đang khởi tạo AI: {settings.PROJECT_NAME}...")

        # Dùng tên model và provider từ config
        self.model = insightface.app.FaceAnalysis(
            name=settings.INSIGHTFACE_MODEL_NAME,
            providers=settings.AI_PROVIDER
        )
        self.model.prepare(ctx_id=0, det_size=(640, 640))
        print("✅ AI Engine đã sẵn sàng!")

    def base64_to_image(self, base64_string):
        if "," in base64_string:
            base64_string = base64_string.split(",")[1]
        image_data = base64.b64decode(base64_string)
        nparr = np.frombuffer(image_data, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    def get_embedding(self, image_base64):
        img = self.base64_to_image(image_base64)
        faces = self.model.get(img)
        if len(faces) == 0:
            return None
        return faces[0].embedding.tolist() # Trả về vector đầu tiên

    def get_raw_embedding(self, image_base64):
        # Hàm này trả về dạng numpy để tính toán
        img = self.base64_to_image(image_base64)
        faces = self.model.get(img)
        if len(faces) == 0:
            return None
        return faces[0].embedding

    @staticmethod
    def compute_similarity(embed1, embed2):
        v1 = np.array(embed1)
        v2 = np.array(embed2)
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Khởi tạo đối tượng toàn cục để dùng chung
ai_service = AIEngine()