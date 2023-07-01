"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys


# replace this comment with your implementation of get_min_payment(),
# interest_due(), remaining_payments(), and main()
def get_min_payment(principle,intrest,term=30,pay=12):
    """ To compute minimum mortgage payment"""
    r = intrest/pay
    form= ((1+ r)**(term *pay))
    upperP = (principle * r* form)

    minPay = upperP/(form -1)
    fin =math.ceil(minPay)

    return fin


def interest_due(balance,intrest,pay=12):
    """ To compute the intrest due"""
    finInt = balance * (intrest/pay)

    return finInt

def remaining_payments(balance,intrest,target,pay=12):
    """ To compute how many payments it would pay to pay off the total balance"""
    
    count = 0

    while balance >0:
       balance -= (target - interest_due(balance,intrest,pay))
       count +=1
    
    return count

def main(principle,intrest,term=30,pay=12,target=None):
    
   
   minPay=  get_min_payment(principle,intrest,term,pay)
   print(minPay)
    
   if(target is None):
    target = minPay
   elif(int(target)<minPay): {
    print("Your target payment is less than the minimum payment for this mortgage")
    }
   else:
    remPay = remaining_payments()

    print(f"If you make payments of ${target}, you will pay off the mortgage in {remPay} payments.")



def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)

    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")

    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)