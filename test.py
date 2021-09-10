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
# start_end=[]
# start_end.append({'x':startPoint[0],'y':startPoint[1]})
# start_end.append({'x':endPoint[0],'y':endPoint[1]})


#找出x or y軸是否有相等，並且存到陣列
isLinked = [] #這裡面都是跟起點同樣x或是y
for pointer in point:
    getPoint = {'x':pointer['x'],'y':pointer['y']}
    if startPoint[0] == getPoint['x'] or startPoint[1] == getPoint['y']:
        isLinked.append(getPoint)
print(isLinked)


#判斷要走x還是y
#找出最近的兩個可走點
pointDistance = []  #用來存點之間的距離
way_1 = []
way_2 = []
temp = []
if isLinked[0]['x'] == isLinked[1]['x']:
    #這邊是x軸相同
    print('x')
    for i in isLinked:
        pointDistance.append(i['y'] - startPoint[1])
        for i in pointDistance:
            temp.append(abs(i))
    way_1.append(pointDistance[temp.index(min(temp))])
else:
    #這邊是y軸相同
    for i in isLinked:
        pointDistance.append(i['x'] - startPoint[0])
        for i in pointDistance:
            temp.append(abs(i))
    way_1.append(pointDistance[temp.index(min(temp))])
    


#找出最小的兩個值的索引值
# way_1 = pointDistance.pop(pointDistance.index(min(pointDistance)))
# way_2 = pointDistance.pop(pointDistance.index(min(pointDistance)))
print(way_1)
# print(way_2)
# print(pointDistance)
