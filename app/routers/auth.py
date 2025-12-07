from fastapi import APIRouter, HTTPException
from app.schemas.user import RegisterRequest, LoginRequest
from app.core.database import load_db, save_db
from app.services.ai_engine import ai_service
from app.core.config import settings

router = APIRouter()


@router.post("/register")
async def register_user(request: RegisterRequest):
    users = load_db()
    if any(u['username'] == request.username for u in users):
        raise HTTPException(status_code=400, detail="Tài khoản đã tồn tại!")

    embedding = ai_service.get_embedding(request.image_base64)
    if not embedding:
        raise HTTPException(status_code=400, detail="Không tìm thấy khuôn mặt!")

    users.append({
        "username": request.username,
        "password": request.password,
        "face_vector": embedding
    })
    save_db(users)
    return {"status": "success", "message": "Đăng ký thành công!"}


@router.post("/login")
async def login_user(request: LoginRequest):
    users = load_db()
    user = next((u for u in users if u['username'] == request.username), None)

    if not user:
        raise HTTPException(status_code=404, detail="Tài khoản không tồn tại!")

    if user['password'] != request.password:
        raise HTTPException(status_code=401, detail="Sai mật khẩu!")

    current_embedding = ai_service.get_embedding(request.image_base64)
    if not current_embedding:
        raise HTTPException(status_code=400, detail="Không tìm thấy khuôn mặt!")

    similarity = ai_service.compute_similarity(user['face_vector'], current_embedding)
    print(f"🔍 Similarity: {similarity}")

    if similarity > settings.FACE_SIMILARITY_THRESHOLD:
        return {"status": "success", "message": "Login OK", "similarity": float(similarity)}

    raise HTTPException(status_code=401, detail="Khuôn mặt không khớp!")