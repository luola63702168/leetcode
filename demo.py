	def xzjz(m):
            if len(m)==0: #若已经没有内圈
                return []
            elif len(m)==1: #若内圈只有一行
                return m[0]
            else: #表明还可以递归内圈
                a=len(m) #当前矩阵行数
                b=len(m[0]) #当前矩阵列数
                c1=[]
                c2=[]
                if b==1: #如果当前矩阵只有一列
                    a=[]
                    for i in m:
                        a.append(i[0])
                    return a #则返回这列元素的列表
                for i in range(1,a-1): #如果有大于一列，这里取(1,a-1)
                                       #是因为外圈两侧避免重复
                        c1.append(m[i][b-1]) #设置外圈右侧列
                        c2.append(m[i][0]) #设置外圈左侧列
                next_m=[] #构建新矩阵，即去除外圈的剩余矩阵
                for j in m[1:-1]: #行少2
                    m1=j[1:-1] #列少2
                    next_m.append(m1)
                return m[0]+c1+m[a-1][::-1]+c2[::-1]+xzjz(next_m) #递归
                #在这里我取一圈的数字，是第一行+右侧外圈[1:-1]+最后一行+左侧
                #外圈[1:-1][::-1],左侧外圈因为是从下往上，所以取反
        return xzjz(matrix)
