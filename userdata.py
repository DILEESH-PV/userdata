import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='userdatadb')
except mysql.connector.Error as e:
    print("db connection error",e)
mycursor=mydb.cursor()
data=requests.get("https://dummyjson.com/users").text
data_info=json.loads(data)
for j in data_info['users']:
    hair=j['hair']
    ch=hair['color']
    try:
        #sql='INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ("'+j['API']+'","'+j['Description']+'","'+j['Auth']+'","'+http+'","'+j['Cors']+'","'+j['Link']+'","'+j['Category']+'")'
        #sql="INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ('"+j['API']+"','"+j['Description']+"','"+j['Auth']+"','"+http+"','"+j['Cors']+"','"+j['Link']+"','"+j['Category']+"')"
        sql="INSERT INTO `userdata`(`first_name`, `last_name`, `maidenName`, `user_name`, `password`, `birthdate`, `hair`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data=(j['firstName'],j['lastName'],j['maidenName'],j['username'],j['password'],j['birthDate'],ch)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully",j['firstName'])
    except mysql.connector.Error as e:
        print("error is",e)
    

        