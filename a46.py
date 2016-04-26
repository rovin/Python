#498.75 desired output
def computepay(h,r):
    if(h <= 40 and h >= 0):
        return h*r
    elif(h > 40):
        sal = ((h - 40)*10.5*1.5) + (40*10.5)
        return sal
    

hrs = float(raw_input("Enter Hours: "))
rte = float(raw_input("Enter Rate: "))
p = computepay(hrs,rte)
print p