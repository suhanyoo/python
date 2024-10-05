#유저 정보 가져오기 DB 연동 한 코드 
import mysql.connector
import random


# UserLogin Function 은 사용자가 로그인 가능 여부 
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

# 사용자가 접속 하면 사용자 ID 를 넣어서 조회 하고 결과를 변수에 담아서 반환 한다. 
#UserLogin("tngks7878","ahemsdl00*")

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

#UserIDSearch("010-3530-3370")

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


#회원가입 로직 
def UserJoin(UserID,UserPW,Name,Phonenumber):
 
    connection = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="ahemsdl00*",
        database ="BingoUserDB"
    )

    cursor = connection.cursor(dictionary=True)

    UserPID = "a1"
    for x in range(6):
        RandomNumber = str(int(random.uniform(1,10)))
        UserPID += RandomNumber

    print(UserPID)
    query = "select * from UserInformation where idUserInformation = %s"
    cursor.execute(query,(UserPID,))

    result = cursor.fetchall()
    
    if len(result) == 0:
        print("ID가 겹치므로 다시 생성 해야 합니다.")
    else:
        print("ID가 겹치지 않음")
    
    query = "Insert into UserInformation (idUserInformation,UserID, UserPW, Name , PhoneNumber) value (%s,%s,%s,%s,%s)"
    cursor.execute(query,(UserPID,UserID,UserPW,Name,Phonenumber,))

    JoinComplete = cursor.fetchall()

    if len(JoinComplete) == 0:
        print("회원가입 성공 ")

    else:
        print("회원가입 실패 ")

UserJoin("tngks7419","z1234","이현정","010-2432-3512")