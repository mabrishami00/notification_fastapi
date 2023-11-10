from fastapi import APIRouter, Body, status, Depends
from fastapi.responses import JSONResponse
from schemas.users import UserEmail, UserInfoEmail
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from core.config import settings
import random
from db.redis import get_redis

router = APIRouter(prefix="/notification")

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=587,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

@router.post("/send_otp", status_code=status.HTTP_200_OK)
async def send_otp(user_email: UserEmail = Body(default=None), redis=Depends(get_redis)):
    try:
        otp_code = random.randint(1000, 9999)
        user_email = user_email.email
        message = MessageSchema(
            subject="OTP Code",
            recipients=[user_email],
            body=f"Your otp code is: {otp_code}",
            subtype=MessageType.plain,
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        await redis.set(user_email, otp_code,ex=120)
        return JSONResponse({"detail": "OTP code has been sent to your email."})
    except:
        return JSONResponse({"detail": "Email has not been sent."}, status_code=status.HTTP_400_BAD_REQUEST)


