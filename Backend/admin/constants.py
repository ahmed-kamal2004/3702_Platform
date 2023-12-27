from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AConstant:
    class TokenINFO:
        SECRET_KEY = """gedsjvndfjknfioewfsdfjkfhjdkfhuyeoihdsjkvcbjcdzbncdsklfjdklf
        dhfklshfdsfjkvhcdnjvkdbnvkjdsvbfkjvbvdsjkvbdckjcdsbvdsjkhfdsvkbvcjksdfbvkjsh
        dbcsdkjbckdsjcvkdsbvkjvbvdsjkvbdfksvbkscjsdjchdsjkvjkvhdfjvkbjkfvbfjkvbfkjbv
        kjsdvbsfdnvdlvnfljvndfvnkldsnfklsgrirtpetjhymjpuomnm,vm.dsfkldfskljdlsfjkkdl
        vklkdsfhkldsfhjkrhjkgfdvfbcvxnmvmncmn,zvdsfjkafjkhhjkfshjkfdsjkdvnsbmvmncxzm
        ,nzcxm,nsdkadshjkjadhkaheehjkerkwtjewrtuyutyirttttttttttttttttttttttttdmvbvv
        c,makjdzxncndksjjccxnjcxzcjshjkdsfahkdfjlsjkl;adscklcnmmcvnmbbmncxvjwedpwejo
        erhdsfiwedoidfnfekbndserblcdsbdfsdbchdfvlbddsnfekdvdfjvghnndfkgjhkfldsghsdlk
        fsdhklfdsjfhklsdfjdfklsnvcjvndskxcdjlkbndfkgjnbfkgjbfgkjdsngsdklfndsfkljsakf
        jsd;fjasl;dfajsdl;asjdasl;jasl;djsl;dfsdferfsondsfklfbvdfcnsdferiofejpdsvndf
        cxklchvfdjghdfkhsdiufsdkfhsdkjfhsadkvgbgerioufhaw9psaodiehfdsolebedferdskjdf"""
        EXPIRETIME_MIN = 15
        ALGORITHM = "HS256"
        ## here I should pass the endpoint of logging
        OAuth2_schema = OAuth2PasswordBearer(tokenUrl="/login/adm")


class TokenInteraction:
    @staticmethod
    def create_token(data: dict) -> dict:
        expire_time = datetime.utcnow() + timedelta(
            minutes=AConstant.TokenINFO.EXPIRETIME_MIN
        )
        data.update({"exp": expire_time})
        token = jwt.encode(
            data,
            AConstant.TokenINFO.SECRET_KEY,
            algorithm=AConstant.TokenINFO.ALGORITHM,
        )

        return token

    @staticmethod
    def verify_token(token: str, exceptions):
        try:
            payload_ = jwt.decode(
                token,
                AConstant.TokenINFO.SECRET_KEY,
                algorithms=[AConstant.TokenINFO.ALGORITHM],
            )
            username = payload_.get("username")
            if not username:
                raise exceptions

            token_data = username=payload_["username"]
            print(token_data)
            return token_data

        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token may be Expired or Invalid",
            )

    @staticmethod
    def get_current_user(token=Depends(AConstant.TokenINFO.OAuth2_schema)):
        print(token)
        exceptions = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )

        return TokenInteraction.verify_token(token, exceptions)




class EmailInteraction:
        subject = "OTP vertification"
        sender_email = "ahmedkamal200427@gmail.com"  ## Must Be changed
        sender_password = None                       ## Must be changed
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        @staticmethod
        def static_constructor(sender_email, sender_password):
            EmailInteraction.sender_email = sender_email
            EmailInteraction.sender_password = sender_password

        @staticmethod
        def send(message: str, receiver) -> bool:
            msg = MIMEMultipart()
            msg["From"] = EmailInteraction.sender_email
            msg["To"] = receiver
            msg["Subject"] = EmailInteraction.subject
            msg.attach(MIMEText(message, "plain"))
            with smtplib.SMTP(
                EmailInteraction.smtp_server,
                EmailInteraction.smtp_port,
            ) as server:
                server.starttls()
                server.login(
                    EmailInteraction.sender_email,
                    EmailInteraction.sender_password,
                )
                server.sendmail(
                    EmailInteraction.sender_email, receiver, msg.as_string()
                )