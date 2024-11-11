def fractional_knapsack(weights,values,capacity):

    res=0
    for pair in sorted(zip(weights,values), key= lambda x: x[1]/x[0], reverse=True):
        if capacity<=0:
            break 
        if pair[0]>capacity:
            res+=float(capacity * (pair[1]/pair[0]))
            capacity=0
        elif pair[0]<=capacity:
            res+=pair[1]
            capacity-=pair[0]
    print(res)        

if __name__=="__main__":
    weights=[]
    values=[]
    items = int(input("Enter no of items :"))
    
    print("Enter Weights....")
    for i in range(items):
        w=int(input("Enter weight :"))
        weights.append(w)
    
    print("Enter values...")
    for i in range(items):
        v=int(input("Enter value :"))
        values.append(v)
    
    capacity=float(input(" Capacity :"))
    print("Filled the bag with objects worth :")
    
    fractional_knapsack(weights,values,capacity)
    
    #weights=[3,3,2,5,1]
    #values=[10,15,10,12,8]
    #capacity=10