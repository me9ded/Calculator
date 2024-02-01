import sys
def double_check(val):
    if 0 <= val <= 9:
        return val
    else:
        raise ValueError(f"{val} not in range[0,9]")
Number1=float(sys.argv[1])
Number2=float(sys.argv[2])
op_selected=str(sys.argv[3])
def add(n1,n2):
    print(f" result: {n1+n2}")
def sub(n1,n2):
    if n1>n2:
        print(f"result: {n1-n2}")
    else:
        print(f"result: {n2-n1}")
def divide(n1,n2):
    if n2==0:
        print("Error cannot divide by 0")
    return(f"result= {n1/n2}")
def multiply(n1,n2):
    print(f"result:{n1*n2}")
def main():
    double_check(Number1)
    double_check(Number2)
    if op_selected=="add":
        add(Number1,Number2)
    if op_selected=="sub":
        sub(Number1,Number2)
    if op_selected=="multiply":
        multiply(Number1,Number2)
    if op_selected=="divide":
        divide(Number1,Number2)
if __name__=="__main__":
    main()
    exit()    