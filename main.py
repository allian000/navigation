import numpy as np
from PIL import Image
im = Image.open("qq.png")   #開啟圖檔
imp = np.array(im)          #換成陣列
#找出所有路線的座標
line = []
for x in range(400):
    for y in range(800):
        if imp[x][y][0] == 0 and imp[x][y][1] == 0 and imp[x][y][2] == 0:
            # temp[x] = y
            tmp = {'x': y, 'y': x}
            line.append(tmp)
#找出所有邊緣的點
'''
line[0] <= now
now = {x: line[0]['x'], y: line[0]['y']}#向右移動
t = {x: line[0]['x'], y: line[0]['y']-1}
b = {x: line[0]['x'], y: line[0]['y']+1}
l = {x: line[0]['x']-1, y: line[0]['y']}
r = {x: line[0]['x']+1, y: line[0]['y']}
if t, b, l, r in line
now is cross road => +
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
#找路線
start=(198,52)
target=(479,251)
fin=[]
fin.append({'x':start[0],'y':start[1]})
fin.append({'x':target[0],'y':target[1]})
min_index = 1
startList=[]
for sta in point:
    location = {'x':sta['x'],'y':sta['y']}
    if start[0] == location['x'] or start[1] == location['y']:
        # print('x: ',location['x'],'y :',location['y'])
        startList.append(location)
# print(startList)
if startList[0]['x'] == startList[1]['x']:  #x軸相同
    print('x is same')
    tmp = []
    for i in startList:
        tmp.append(abs(i['x'] - fin[0]['x']))
        min_val = min(tmp)
        min_index = tmp.index(min_val)
else:
    print('y is same')                      #y軸相同
    tmp = []
    for i in startList:
        tmp.append(abs(i['x'] - fin[0]['x']))
        min_val = min(tmp)
        min_index = tmp.index(min_val)
#走路徑
load = []
load.append(startList[min_index])
for lo in point:
    if lo['x'] == load[len(load)-1]['x']:
        load.append(lo)
    if lo['y'] == load[len(load)-1]['y']:
        load.append(lo)

print(load)
# print(point)[1,2,3]
# for find in point:
#     rightSide = {'x': find['x']+1, 'y': find['y']}    #向右移動
#     topSide = {'x': find['x'], 'y': find['y']-1}      #向下移動
#     bottomSide = {'x': find['x'], 'y': find['y']+1}   #向上移動
#     leftSide = {'x': find['x']-1, 'y': find['y']}     #向左移動
# print(point)
