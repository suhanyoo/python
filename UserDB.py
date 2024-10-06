#유저 정보 가져오기 DB 연동 한 코드 
import mysql.connector
import random
import re


#로그인  
def UserLogin(userid,userpw):
    connection = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="ahemsdl00*",
        database ="BingoUserDB"
    )
    cursor = connection.cursor(dictionary=True)

    # query 변수에 담아서 SQL 인잭션 방지 하여서 파라미터 바인딩 
    query = "select * from UserInformation where UserID = %s and UserPW = %s"
    cursor.execute(query,(userid,userpw,))

    #fetchall 은 결과를 리스트로 반환 하여 반복하면서 각 행을 출력 하는 용도 
    result = cursor.fetchall()

    if len(result) == 0:
        print("아이디 또는 비밀번호가 틀렸습니다.")
    else:
        print("로그인 성공 하셨습니다")

    cursor.close()
    connection.close()

#아이디 찾기 
def UserIDSearch(Userphonenumber):
    
    connection = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="ahemsdl00*",
        database ="BingoUserDB"
    )
    cursor = connection.cursor(dictionary=True)

    # query 변수에 담아서 SQL 인잭션 방지 하여서 파라미터 바인딩 
    query = "select * from UserInformation where PhoneNumber = %s"
    cursor.execute(query,(Userphonenumber,))

    result = cursor.fetchall()

    if len(result) == 0:
        print("가입된 회원 정보가 없습니다. 회원가입 해주세요")
    else:
        for x in result:
            print(x['UserID'])

#비밀번호 찾기 
def UserSearchPW(UserID):
    
    connection = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="ahemsdl00*",
        database ="BingoUserDB"
    )
    cursor = connection.cursor(dictionary=True)

    # query 변수에 담아서 SQL 인잭션 방지 하여서 파라미터 바인딩 
    query = "select * from UserInformation where UserID = %s"
    cursor.execute(query,(UserID,))

    result = cursor.fetchall()

    if len(result) == 0:
        print("해당 아이디의 비밀번호를 찾을 수가 없습니다.")
    else:
        for x in result:
            print(x['UserPW'])
    
    cursor.close()
    connection.close()


#회원가입 
def UserJoin(UserID,UserPW,Name,Phonenumber):
    JoinIDResult = False

    connection = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="ahemsdl00*",
        database ="BingoUserDB"
    )
    cursor = connection.cursor(dictionary=True)

    # User ID 생성 후 조회 하여 ID 중복 여부 확인 하는 로직 
    for x in range(6):
        UserPID = "a1"
        for x in range(6):
            RandomNumber = str(int(random.uniform(1,10)))
            UserPID += RandomNumber

        query = "select * from UserInformation where idUserInformation = %s"
        cursor.execute(query,(UserPID,))
        result = cursor.fetchall()
        
    # ID 값을 조회 하여 중복 된 ID가 있는지 확인 
        if len(result) == 0:
            JoinIDResult = False
            break
        else:
            JoinIDResult = True
        

    # ID 중복 된 값 의 진위 여부에 따른 회원정보 넣기 
    if JoinIDResult == True:
        print(JoinIDResult)
    else:
        query = "Insert into UserInformation (idUserInformation,UserID, UserPW, Name , PhoneNumber) value (%s,%s,%s,%s,%s)"
        cursor.execute(query,(UserPID,UserID,UserPW,Name,Phonenumber,))
        connection.commit()
    
    cursor.close()
    connection.close()

#비밀번호 변경 
def UserPasswordExcahge(phonenumber,NewPassword):
    
    # 비밀번호 특수문자 여부 확인 
    global NewPasswordResult
    NewPasswordResult = False
    Patten = r"[\.\!\@\#\$\%\^\&\*\(\)\-\\]"
    matches = re.findall(Patten,NewPassword)
    
    if len(matches) > 0:
        NewPasswordResult = True
        return NewPasswordResult
    else:
        NewPasswordResult = False

    connection = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "ahemsdl00*",
        database = "BingoUserDB"
    )

    cursor = connection.cursor(dictionary=True)

    query = "update UserInformation set UserPW = %s where PhoneNumber = %s"
    cursor.execute(query,(NewPassword,phonenumber,))
    cursor.fetchall()
    connection.commit()

    cursor.close()
    connection.close()



