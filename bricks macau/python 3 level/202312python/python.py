import os
import csv



def p6():

    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    print('current_directory',current_directory)

    file_path = os.path.join(current_directory, 'cai.csv')

    f = open(file_path, 'r',encoding='utf-8')




    # 獲得每行代碼的內容
    for i in f:
        print(i.strip())


    c = []
    for i in f:
        # strip 刪除 string 頭尾的空格,包括 \n \tab. split 把一個 string 轉換成 list.
        c.append(i.strip('\n').split(','))
    f.close()
    print(c)


def p7():
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    file_path = os.path.join(current_directory, 'abc.txt')

    f = open(file_path,'r',encoding='utf-8')
    s = f.readlines()
    # s = f.read()
    print(s)



def insertion_sort(arr):

    # 從第二個元素開始，假設第一個元素已經排序
    for i in range(1, len(arr)):

        key = arr[i]  # 當前要插入的元素
        j = i - 1  # 已排序部分的最後一個元素的索引
        
        # 將key插入到已排序的部分
        while j >= 0 and key < arr[j]:  # 如果key小於當前已排序元素，則繼續移動.
            arr[j + 1] = arr[j]  # 將較大的元素向後移動一位
            j -= 1  # 繼續向前比較
        
        arr[j + 1] = key  # 將key插入到正確位置

# 測試範例
# arr = [12, 11, 13, 5, 6]
# print("排序前的陣列:", arr)
# insertion_sort(arr)
# print("排序後的陣列:", arr)

def p29():
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    file_path = os.path.join(current_directory, 'shuiguo.csv')

    shuig=['苹果','香蕉','桃子','西瓜']
    f=open(file_path,'w',encoding='utf-8')
    f.write(','.join(shuig)+'\n')
    # f.write(','.join(shuig))
    f.close()



a = any([None,[],(),{}])
print(a)

