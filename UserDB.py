#유저 정보 가져오기 DB 연동 한 코드 
import mysql.connector

def UserLogin(userid):
    connection = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="ahemsdl00*",
        database ="BingoUserDB"
    )
    cursor = connection.cursor(dictionary=True)

    # query 변수에 담아서 SQL 인잭션 방지 하여서 파라미터 바인딩 
    query = "select * from UserInformation where UserID = %s"
    cursor.execute(query,(userid,))

    #fetchall 은 결과를 리스트로 반환 하여 반복하면서 각 행을 출력 하는 용도 
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()

# 사용자가 접속 하면 사용자 ID 를 넣어서 조회 하고 결과를 변수에 담아서 반환 한다. 
UserLogin("tngks7878")





