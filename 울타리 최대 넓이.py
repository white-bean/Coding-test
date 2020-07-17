# 울타리에서 나올 수 있는 최대 크기의 직사각형 넓이 구하기

# 분할정복
def fence(left,right):
    if  left==right:  #판자가 하나일 경우 
        return h[left]
    mid=(left+right)/2 # 두 구간으로 분할
    tmp=max(fence(left,mid),fence(mid+1,right)) #양쪽 문제를 해결
    
    #가운데 부분
    low=mid
    high=mid+1
    height=min(h[low],h[high])
    tmp=max(tmp,height*2) #mid~mid+1 인 사각형
    
    #확장
    while left<low or high<right:
        if hi<right and (low == left or h[low-1]<h[high+1]) # 오른쪽으로 진행해야하는 경우
            high+=1
            height=min(height,h[high])
        else: # 왼쪽 진행
            low-=1
            height=min(height,h[low])
        tmp=max(tmp,height*(high-low+1))

    return tmp


# 완전 탐색
def fence(h):
    tmp=0
    n=len(h)

    for left in range(0,n,1):
        minH=h[left]
        for right in range(0,n,1):
            minH=min(minH,h[right])
            tmp=max(tmp,(right-left+1)*minH)
    
    return tmp
