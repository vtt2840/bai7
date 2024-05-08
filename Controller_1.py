# Nhập các thư viện cần thiết
import json
from array import array
from builtins import print, map, format
from operator import index

from scipy.constants import value

from Impact import Impact

# đối tượng cảm xúc
class Emotion:
    pleasure = 0.75
    surprise = 0.5
    anger = -0.2
    fear = -0.2
    hate = -0.4
    sad = -0.4
    def getLstEmotion(self):
        return [self.pleasure, self.surprise, self.anger, self.fear, self.hate, self.sad]

#tính các N ( số người theo nhóm )
nChildren = nALKW = nBFGMEN = nElder = nBlinder = nOther = 0

with open("Pedestrians.json", 'r') as file:
    data = json.load(file)

for obj_Pedestrian in data:
    age = obj_Pedestrian["age"]
    if age < 12:
        nChildren += 1
    if age > 60:
        nElder += 1
    if 12 < age < 60:
        nOther += 1
    velocity = obj_Pedestrian["velocity"]
    if velocity == 0.52:
        nBlinder += 1
        nOther -= 1
    start = obj_Pedestrian["wardDistribution"]
    if start == "A" or start == "L" or start == "K" or start == "W":
        nALKW += 1
        nOther -= 1
    if start == "B" or start == "F" or start == "M" or start == "G" or start == "E" or start == "N":
        nBFGMEN += 1
        nOther -= 1

# đọc lấy impactOfAGV
def read_json_file():
    # Đường dẫn tới tệp JSON cần đọc
    file_path = 'input.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data["impactOfAGV"]["distribution"]

def impactToChildren(n):
    data = read_json_file()["children"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactChildren = Impact(n, k, min, max)
    return impactChildren.getImpact()

def impactToALKW(n):
    data = read_json_file()["ALKW"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactALKW = Impact(n, k, min, max)
    return impactALKW.getImpact()

def impactToBFGMEN(n):
    data = read_json_file()["BFGMEN"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBFGMEN = Impact(n, k, min, max)
    return impactBFGMEN.getImpact()

def impactToElder(n):
    data = read_json_file()["Elder"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBFGMEN = Impact(n, k, min, max)
    return impactBFGMEN.getImpact()

def impactToBlinder(n):
    data = read_json_file()["Blinder"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBlinder = Impact(n, k, min, max)
    return impactBlinder.getImpact()

def impactToOthers(n):
    data = read_json_file()["Other"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactOthers = Impact(n, k, min, max)
    return impactOthers.getImpact()

# tạo mảng 2 chiều 6*N với n là số lượng Pedestrian theo đối tượng
def create_2d_array(n):
    array_2d = [[0] * n for _ in range(6)]
    return array_2d

# hàm tìm gía trị gần nhất
def find_closest_value(target, lst):
    closest_value = None
    min_difference = float('inf')  # Đặt giá trị khởi tạo là vô cùng lớn
    for value in lst:
        difference = abs(target - value)
        if difference < min_difference:
            min_difference = difference
            closest_value = value
    return closest_value

# tạo obj emotion lấy giá trị cảm xúc gần nhất
ex1 = Emotion()
closest_value = find_closest_value(0.1, ex1.getLstEmotion())
print("Giá trị gần nhất là:", closest_value)

# tạo các giá trị ngẩu nhiên
impactToChildren(nChildren)
impactToALKW(nALKW)
impactToBFGMEN(nBFGMEN)
impactToOthers(nOther)
impactToElder(nElder)
impactToBlinder(nBlinder)

mapped_array = []
# Thay đổi các giá trị trong mảng thành giá trị gần nhất đã cho
print("========= Giá trị cảm xúc theo 6 loại ===============>>>> ")
for value in arr:
    x = find_closest_value(value, ex1.getLstEmotion())
    mapped_array.append(x)
print(mapped_array)
