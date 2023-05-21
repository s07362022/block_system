import numpy as np
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
cursor = connection.cursor(buffered=True)

posi_keys =[{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
x,y,w,h = 10,10,10,10
color_list = ['r','b','g','ye']
for i in range(5):
   x_center=(x+w)//2
   y_center = (y+h)//2
   posi_keys[i]= {'position':'%s,%s' %(x_center,y_center),
                  'color':'%s'%(color_list[0])
   }
   x,y,w,h = x+10,y+10,w+10,h+10
posi_list = []
print(posi_keys)
for i in range(len(posi_keys)):
   if posi_keys[i] != {}:
        p=posi_keys[i]#['position']
        # print(p.split(',')[0])
        print(p['position']+','+p['color']) #INSERT INTO %s VALUES (%s)"%(TableName,ROWstr[:-1])
        posi_list.append(p['position']+','+p['color'])
   else:
       posi_list.append('')
print(len(posi_list[:]))
cursor.execute( '''INSERT INTO posiseat (`one`,`two`,`three`,`four`,`five`,`six`,`seven`,`eight`,`nine`,`ten`,`eleven`
                                ,`twelve`,`thirteen`,`fourteen`,`fifteen`,`sixteen`,`seventeen`,`eighteen`,`nineteen`,
                                `twenty`,`twenty-one`,`twenty-two`,`twenty-three`,`twenty-four`,`twenty-five`,`twenty-six`,`twenty-seven`,
                                `twenty-eight`,`twenty-nine`,`thirty`,`thirty-one`,`thirty-two`,`thirty-three`
                                ,`thirty-four`,`thirty-five`,`thirty-six`                                        
                                ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''', (posi_list[:]))

connection.commit()                                                                      
# QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(box_count),t,start_timeall,end_time_all)
command = "SELECT * FROM posiseat "
# 執行指令
cursor.execute(command)

result = cursor.fetchall()
if len(result)>=2:
    second_last_row = [*result[-2]]
    second_last_row.pop(0)
    print(second_last_row)

    last2_x_list=[]
    last2_y_list=[]
    last2_color_list=[]
    for k in range(len(second_last_row)):# 
        if (second_last_row[k]!='' ):
            second_last_element= second_last_row[k].split(',')
            last2_x_list.append(second_last_element[0])
            last2_y_list.append(second_last_element[1])
            last2_color_list.append(second_last_element[2])
    print(last2_x_list)
# print(result)
# cursor.execute(SS)