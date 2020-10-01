def solution(w,h):
    def gcd(x, y):
        if y == 0: 
            return x
        return gcd(y, x%y)
    
    return w*h-(w+h-gcd(max(w,h),min(w,h)))
