from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random

from . import models, schemas, security
from .database import get_db
from .notifications import send_otp_email

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

def generate_otp():
    return str(random.randint(100000, 999999))

def handle_email_sending(email: str, otp: str):
    """Helper function to send email and handle errors."""
    email_result = send_otp_email(recipient_email=email, otp=otp)
    if email_result.get("status") == "error":
        # This indicates a server-side configuration issue.
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Email service is currently unavailable. Please try again later."
        )

@router.post("/signup/initiate", response_model=schemas.Msg)
def initiate_signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    otp = generate_otp()
    otp_expires_at = datetime.utcnow() + timedelta(minutes=10)
    hashed_password = security.get_password_hash(user.password)

    new_user = models.User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        phone=user.phone,
        otp=otp,
        otp_expires_at=otp_expires_at,
        is_admin=user.is_admin # Set to True for admin signup
    )
    db.add(new_user)
    handle_email_sending(user.email, otp)
    db.commit()
    
    return {"msg": "OTP sent to your email for verification."}

@router.post("/signup/verify", response_model=schemas.Token)
def verify_signup(data: schemas.OtpVerify, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    if user.is_verified:
        raise HTTPException(status_code=400, detail="Account already verified.")

    if user.otp != data.otp or user.otp_expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired OTP.")

    user.is_verified = True
    user.otp = None
    user.otp_expires_at = None
    db.commit()
    db.refresh(user)

    access_token = security.create_access_token(data={"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id, "is_admin": user.is_admin}


@router.post("/login/initiate", response_model=schemas.Msg)
def initiate_login(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.email).first()

    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Account not verified. Please complete the signup process.")

    otp = generate_otp()
    user.otp = otp
    user.otp_expires_at = datetime.utcnow() + timedelta(minutes=10)
    
    handle_email_sending(user.email, otp)
    db.commit()

    return {"msg": "OTP sent to your email for 2FA."}


@router.post("/login/verify", response_model=schemas.Token)
def verify_login(data: schemas.OtpVerify, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    if user.otp != data.otp or user.otp_expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired OTP.")

    user.otp = None
    user.otp_expires_at = None
    user.last_login = datetime.utcnow()
    db.commit()
    db.refresh(user)

    access_token = security.create_access_token(data={"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id, "is_admin": user.is_admin}


@router.post("/otp/resend", response_model=schemas.Msg)
def resend_otp(data: schemas.Email, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    otp = generate_otp()
    user.otp = otp
    user.otp_expires_at = datetime.utcnow() + timedelta(minutes=10)

    handle_email_sending(user.email, otp)
    db.commit()

    return {"msg": "A new OTP has been sent to your email."}

@router.post("/password-reset/initiate", response_model=schemas.Msg)
def initiate_password_reset(data: schemas.Email, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        # To prevent email enumeration, return a generic success message even if the user doesn't exist.
        return {"msg": "If an account with this email exists, a password reset OTP has been sent."}

    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Account not verified. Please verify your account first.")

    otp = generate_otp()
    user.otp = otp
    user.otp_expires_at = datetime.utcnow() + timedelta(minutes=10)
    
    handle_email_sending(user.email, otp)
    db.commit()

    return {"msg": "If an account with this email exists, a password reset OTP has been sent."}

@router.post("/password-reset/complete", response_model=schemas.Msg)
def complete_password_reset(data: schemas.PasswordResetComplete, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    if user.otp != data.otp or user.otp_expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired OTP.")

    user.hashed_password = security.get_password_hash(data.new_password)
    user.otp = None
    user.otp_expires_at = None
    db.commit()

    return {"msg": "Password has been reset successfully. You can now log in."}