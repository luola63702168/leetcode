class BestStock(object):
    '''买股票的最佳时机'''
    def stock(self,para):
        profit=0
        for i in range(len(para)-1):
            # print(i,len(para))
            if para[i]<para[i+1]:
                profit += para[i+1]-para[i]
                # print(profit)
        return profit
l=BestStock()
t=l.stock([7,1,5,3,6,4])
print(t)

