from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import string
import random


class PConstant:
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
        OAuth2_schema = OAuth2PasswordBearer(tokenUrl="/login/pub")


class TokenInteraction:
    @staticmethod
    def create_token(data: dict) -> dict:
        expire_time = datetime.utcnow() + timedelta(
            minutes=PConstant.TokenINFO.EXPIRETIME_MIN
        )
        data.update({"exp": expire_time})
        token = jwt.encode(
            data,
            PConstant.TokenINFO.SECRET_KEY,
            algorithm=PConstant.TokenINFO.ALGORITHM,
        )

        return token

    @staticmethod
    def verify_token(token: str, exceptions):
        try:
            payload_ = jwt.decode(
                token,
                PConstant.TokenINFO.SECRET_KEY,
                algorithms=[PConstant.TokenINFO.ALGORITHM],
            )
            username = payload_.get("username")
            if not username:
                raise exceptions

            username = payload_["username"]
            return username

        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token may be Expired or Invalid",
            )

    @staticmethod
    def get_current_user(token=Depends(PConstant.TokenINFO.OAuth2_schema)):
        print(token)
        exceptions = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )

        return TokenInteraction.verify_token(token, exceptions)


# class GenerateCode:
#     length = 20

#     @staticmethod
#     def generate_code() -> str:
#         letters = string.ascii_lowercase
#         letters += string.ascii_uppercase
#         result_str = "".join(random.choice(letters) for i in range(GenerateCode.length))
#         return result_str
