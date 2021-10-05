import numpy as np
from PIL import Image
im = Image.open("qq.png")   #開啟圖檔
imp = np.array(im)          #換成陣列
#找出所有路線的座標
'''
找出所有路線的座標
將 x 和 y 值讀取進來
檢查每一個座標點的RGB值
如果為黑色就存進line
'''
line = []
for x in range(400):
    for y in range(800):
        if imp[x][y][0] == 0 and imp[x][y][1] == 0 and imp[x][y][2] == 0:
            # temp[x] = y
            tmp = {'x': y, 'y': x}
            line.append(tmp)
#找出所有邊緣的點
'''
now is cross road => +
這邊把所有相鄰的點記錄起來
'''
point = []
def findRoad(line, top, bottom, left, right):
    topWay = top in line
    bottomWay = bottom in line
    rightWay = right in line
    leftWay = left in line
    topANDbottom = topWay or bottomWay
    rightANDleft = rightWay or leftWay
    return topANDbottom and rightANDleft
for now in line:
    rightSide = {'x': now['x']+1, 'y': now['y']}    #向右移動
    topSide = {'x': now['x'], 'y': now['y']-1}      #向下移動
    bottomSide = {'x': now['x'], 'y': now['y']+1}   #向上移動
    leftSide = {'x': now['x']-1, 'y': now['y']}     #向左移動
    if (findRoad(line, topSide,bottomSide,leftSide,rightSide)):
        point.append(now)
################################################################
#設起始點 startPoint = (198,52),目標點 endPoint = (479,251)
startPoint = (198,52)
endPoint = (479,251)
#將終點塞到所有關聯點內
point.append({'x':endPoint[0],'y':endPoint[1]})
##################################################
queue=[]
seen=[]
road=[]
#起點先加進來
s = {'x':startPoint[0],'y':startPoint[1]}
queue.append(s)
seen.append(s)
#開始找相鄰的點
#找x or y相同的放進暫存裡
#BFS原則
while (len(queue) > 0):
    vertex = queue.pop(0)
    #將所有與vertex相鄰的連接點放進來
    link=[]
    #離結點最近的可能是有連接?
    for i in point:
        if vertex['y'] == i['y'] or vertex['x'] == i['x']:
            link.append(i)
    nodes = link
    for w in nodes:
        if w not in seen:
            queue.append(w)
            seen.append(w)
            if w['x'] == endPoint[0] and w['y'] == endPoint[1]:
                break
    road.append(vertex)
for i in road:
    print(i)
