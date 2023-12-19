from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .schemas import TokenModel, TokenDataModel
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


class Constant:
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
        OAuth2_schema = OAuth2PasswordBearer(tokenUrl="/login")


class PasswordInteraction:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash_password(password: str) -> str:
        return PasswordInteraction.pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return PasswordInteraction.pwd_context.verify(password, hashed_password)


class TokenInteraction:
    @staticmethod
    def create_token(data: dict) -> dict:
        expire_time = datetime.utcnow() + timedelta(
            minutes=Constant.TokenINFO.EXPIRETIME_MIN
        )
        data.update({"exp": expire_time})
        token = jwt.encode(
            data,
            Constant.TokenINFO.SECRET_KEY,
            algorithm=Constant.TokenINFO.ALGORITHM,
        )

        return token

    @staticmethod
    def verify_token(token: str, exceptions):
        try:
            payload_ = jwt.decode(
                token,
                Constant.TokenINFO.SECRET_KEY,
                algorithms=[Constant.TokenINFO.ALGORITHM],
            )
            id = payload_.get("id")
            print(id)
            if not id:
                raise exceptions

            token_data = TokenDataModel(id=payload_["id"])
            print(token_data)
            return token_data

        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token may be Expired or Invalid",
            )

    @staticmethod
    def get_current_user(token=Depends(Constant.TokenINFO.OAuth2_schema)):
        print(token)
        exceptions = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )

        return TokenInteraction.verify_token(token, exceptions)
