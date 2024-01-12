f = open('./Input.txt', 'r')
Input = f.readlines()
f.close()
#打開文件、讀取文件、關閉文件

def initialize_main(temp, line_number=5):  #行號 5
    temp = temp.replace('\n', '').split(' ')  # 從文件的第一行（Input[0]）中讀取數據，去除換行符，然後以空格分割成列表
    
    if len(temp) == 3:      # 檢查 temp 列表的長度是否為 3
        return [[line_number, temp[0], temp[1], temp[2]]]
        # 如果是，則初始化主列表 main，其中包含一個元素，該元素是一個包含 4 個元素的列表
        # 這個列表的元素分別是行號 5，temp[0]，temp[1]，temp[2]

    else:
        return [[line_number, '', temp[0], temp[1]]]   # 如果否，這個列表的元素分別是行號 5，空字符串，temp[0]，temp[1]

def initialize_macro():    
    return {}, [False, '']
# 返回一個元組，包含一個空字典和一個包含兩個元素的列表，用於初始化巨集字典和 in_macro 標誌。

line = 5 #行號的起始值
for i in Input[1:]:     # 迭代文件中的每一行
    line += 5          # 將行號增加 5

    if (i[0] == '.'):
        continue
    # 如果以 '.' 開頭，表示是註釋，則跳過當前迭代
    
    i = i.replace('\n', '').split(' ')
    # 將當前行去除換行符，然後以空格分割成列表

    if (len(i) == 1):
        now = [line, '', i[0], '']
# 如果當前行的元素個數為 1，初始化列表 'now'，包含行號、空字符串、第一個元素（i[0]），空字符串
    elif (len(i) == 2):
        now = [line, '', i[0], i[1]]
# 元素個數為 2，'now'，包含行號、空字符串、第一個元素（i[0]），第二個元素（i[1]）
    else:
        now = [line, i[0], i[1], i[2]]
# 元素個數為 3，'now'，包含行號、第一個元素（i[0]），第二個元素（i[1]），第三個元素（i[2]）

    # 根據 'now' 中的第三個元素進行不同的處理
    if (now[2] == 'MACRO'):     # 如果是 'MACRO'，設置標誌表示現在處於巨集定義內部，並在巨集字典中初始化相應的值
        in_macro = [True, now[1]]  
        macro[now[1]] = [now[3].split(','), []]  #以巨集名稱為鍵初始化一個值，該值是一個包含參數列表和展開行的列表
        continue       #跳過當前迭代，繼續處理下一行
        
    elif (now[2] == 'MEND'):
        in_macro = [False, '']
        continue
# 如果是 'MEND'，設置標誌表示現在不再處於巨集定義內部，將當前巨集的名稱設置為空字符串，繼續處理下一行
    
    if in_macro[0]:   # 如果當前處於巨集定義內部
        macro[in_macro[1]][1].append(now)   # 將當前行添加到巨集的展開行中
    else:
        if now[2] in macro:    # 如果當前行的第三個元素在 'macro' 中
            function_ = now[1]    # 提取當前行的函數名稱

            if (now[1]) != '':
                now[1] = f'.{now[1]}'
            # 如果函數名稱不為空，將其修改為以點開頭的形式
            
            main.append(now.copy()) # 將當前行的副本添加到主列表 'main'
            
            parms = {}
            now[3] = now[3].split(',')    # 將當前行的第四個元素（參數列表）以逗號分割成列表
            for n, p in enumerate(macro[now[2]][0]):
                parms[p] = now[3][n]
            # 對巨集定義中的參數和當前行的參數進行一一對應
            
            macro[now[2]][1][0][1] = function_       # 修改巨集定義中展開行的函數名稱
            10s"%('Line', '', 'Original', ''))
# 打印最終的輸出，包括格式化的行
            for n, j in enumerate(macro[now[2]][1]):     # 遍歷巨集的展開行
                j = j.copy()    # 複製展開行
                j[0] = str(line) + chr(ord('a')+n)   # 修改展開行的行號，使用當前行的行號和字母 'a' 到 'z' 之間的字符
                
                for k in parms.keys():
                    if k in j[3]:
                        j[3] = j[3].replace(k, parms[k])
              # 對展開行中的參數進行替換

                main.append(j.copy())   # 將替換後的展開行的副本添加到主列表 'main'

        else:
            main.append(now)
       # 如果當前行不是巨集調用，將當前行的副本添加到主列表 'main'

print(" %-10s %-10s %-10s %-號、巨集名稱和它們對應的展開行

for i in main:    # 迭代主列表 'main'
    if (i[1] == '.'):     # 判斷當前行的第二個元素是否為 '.'，表示該行是註釋
        print(" %-10s %-10s %-10s %-39s"%(i[0], i[1], i[2], i[3]))  # 如果是註釋，以格式化的方式打印行號、空字符串、原始代碼的第一個元素（i[2]）、原始代碼的第二個元素（i[3]）
    else: 
        print(" %-10s %-10s %-10s %-10s"%(i[0], i[1], i[2], i[3]))   # 如果不是註釋，以格式化的方式打印行號、原始代碼的第一個元素（i[1]）、原始代碼的第二個元素（i[2]）、原始代碼的第三個元素（i[3]）
