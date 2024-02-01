import argparse
def double_check(val):
    ivalue=float(val)
    if 0 <= ivalue <= 9:
        return ivalue
    else:
        raise argparse.ArgumentTypeError(f'{val} is not in range [0,9]')
parser=argparse.ArgumentParser(description="calculator")
parser.add_argument('--number1',type=double_check,required=True,help='enter the first number in [0,9]')
parser.add_argument('--number2',type=double_check,required=True,help='enter the second numbe in [0,9]')
parser.add_argument('--operatorselected',type=str,help='Enter the desired operator you want to use')
args=parser.parse_args()
number1=args.number1
number2=args.number2
op_selected=args.operatorselected
print(f'Entered numbers:{number1},{number2}')
def add(N1,N2):
    a=N1+N2
    print(f"result: {a}")
def sub(N1,N2):
    if N1>=N2:
        print(f"result: {N1-N2}")
    else:
        print(N2-N1)
def multiply(N1,N2):
    if N1==0 or N2==0:
        print(f"result: {0}")
    else:
        print(f"result: {N1*N2}")
def divide(N1,N2):
    if N2!=0:
        print(f"result: {N1/N2}")
    else:
        print("Error You cannot divide by 0")
def main():
    print(f"N1: {args.number1}")
    print(f"N2: {args.number2}")
    double_check(args.number1)
    double_check(args.number2)
    if op_selected=="add":
        add(args.number1,args.number2)
    if op_selected=="sub":
        sub(args.number1,args.number2)
    if op_selected=="multiply":
        multiply(args.number1,args.number2)
    if op_selected=="divide":
        divide(args.number1,args.number2)
if __name__=="__main__":
    main()
    exit()


    