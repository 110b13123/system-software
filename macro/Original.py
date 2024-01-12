# 打開文件、讀取文件、關閉文件
f = open('./Input.txt', 'r')
Input = f.readlines()
f.close()

# 行號 5
def initialize_main(temp, line_number=5):  
    # 從文件的第一行（Input[0]）中讀取數據，去除換行符，然後以空格分割成列表
    temp = temp.replace('\n', '').split(' ')  
    
    # 檢查 temp 列表的長度是否為 3
    if len(temp) == 3:      
        # 如果是，則初始化主列表 main，其中包含一個元素，該元素是一個包含 4 個元素的列表
        # 這個列表的元素分別是行號 5，temp[0]，temp[1]，temp[2]
        return [[line_number, temp[0], temp[1], temp[2]]]
    else:
        # 如果否，這個列表的元素分別是行號 5，空字符串，temp[0]，temp[1]
        return [[line_number, '', temp[0], temp[1]]]   

# 返回一個元組，包含一個空字典和一個包含兩個元素的列表，用於初始化巨集字典和 in_macro 標誌。
def initialize_macro():    
    return {}, [False, '']

# 初始化行號
line = 5

# 遍歷文件的每一行
for i in Input[1:]:
    line += 5

    # 如果以 '.' 開頭，表示是註釋，則跳過當前迭代
    if (i[0] == '.'):
        continue

    # 將當前行去除換行符，然後以空格分割成列表
    i = i.replace('\n', '').split(' ')

    # 根據列表的長度初始化當前行的格式
    if (len(i) == 1):
        now = [line, '', i[0], '']
    elif (len(i) == 2):
        now = [line, '', i[0], i[1]]
    else:
        now = [line, i[0], i[1], i[2]]

    # 根據當前行的第三個元素進行不同的處理
    if (now[2] == 'MACRO'):     
        # 如果是 'MACRO'，設置標誌表示現在處於巨集定義內部，並在巨集字典中初始化相應的值
        in_macro = [True, now[1]]
        macro[now[1]] = [now[3].split(','), []]
        continue
    elif (now[2] == 'MEND'):
        # 如果是 'MEND'，設置標誌表示現在不再處於巨集定義內部，將當前巨集的名稱設置為空字符串
        in_macro = [False, '']
        continue

    if in_macro[0]:   
        # 如果當前處於巨集定義內部
        macro[in_macro[1]][1].append(now)
    else:
        if now[2] in macro:
            # 如果當前行的第三個元素在 'macro' 中
            function_ = now[1]

            if (now[1]) != '':
                now[1] = f'.{now[1]}'
            
            main.append(now.copy())
            
            parms = {}
            now[3] = now[3].split(',')
            for n, p in enumerate(macro[now[2]][0]):
                parms[p] = now[3][n]
            
            macro[now[2]][1][0][1] = function_
            for n, j in enumerate(macro[now[2]][1]):
                j = j.copy()
                j[0] = str(line) + chr(ord('a')+n)
                for k in parms.keys():
                    if k in j[3]:
                        j[3] = j[3].replace(k, parms[k])

                main.append(j.copy())

        else:
            main.append(now)


# 打印最終的輸出，包括格式化的行號、巨集名稱和它們對應的展開行
print(" %-10s %-10s %-10s %-10s"%('Line', '', 'Original', ''))
for i in main:
    if (i[1] == '.'):
        print(" %-10s %-10s %-10s %-39s"%(i[0], i[1], i[2], i[3]))
    else:
        print(" %-10s %-10s %-10s %-10s"%(i[0], i[1], i[2], i[3]))
