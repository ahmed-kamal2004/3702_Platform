from datetime import date


class Query:
    pass


class NonQuery:
    ################################            INSERTIONS =================================           ################################
    @staticmethod
    def new_admin(
        username: str, email: str, password: str, dob: date, phonenumber: str
    ) -> str:
        query = f"""INSERT INTO Admin (username,email,password,DOB,phonenumber) VALUES({username}, {email}, {password}, {dob}, {phonenumber});"""
        return query

    @staticmethod
    def new_student(
        username: str,
        email: str,
        password: str,
        is_active: bool,
        photo: str,
        dob: date,
        nickname: str,
        phonenumber: str,
    ) -> list[str, str]:
        first_query = f"""INSERT INTO user (username,email,password,is_active,photo,DOB,nickname,phonenumber)
        VALUES ({username}, {email}, {password}, {is_active}, {photo}, {dob}, {nickname}, {phonenumber});"""
        second_query = f"""INSERT INTO student (username) VALUES ({username});"""
        return [first_query, second_query]

    @staticmethod
    def new_publisher(
        username: str,
        email: str,
        password: str,
        is_active: bool,
        photo: str,
        dob: date,
        nickname: str,
        phonenumber: str,
        linked_url: str,
        job: str,
    ) -> list[str, str]:
        first_query = f"""INSERT INTO user (username,email,password,is_active,photo,DOB,nickname,phonenumber)
        VALUES ({username}, {email}, {password}, {is_active}, {photo}, {dob}, {nickname}, {phonenumber});"""
        second_query = f"""INSERT INTO publisher (username,linked_url,job) VALUES ({username},{linked_url},{job});"""
        return [first_query, second_query]
