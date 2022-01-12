import argparse

import math
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str, required=True)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int,)
parser.add_argument('--interest', type=float, help="Incorrect parameters")
parser.add_argument('--payment', type=float,)
args = parser.parse_args()
alist = []

if args.interest is None:
    print("Incorrect parameters")
    exit()

for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))

dif_month = 1
overpay = 0
m = ''
y = ''


if alist[0] == 'diff':
    if args.interest is None or args.type not in alist or len(alist) != 4:
        print("Incorrect parameters")
        exit()
    elif args.payment in alist:
        print("Incorrect parameters")
    elif alist[1] < 0 or alist[2] < 0 or alist[3] < 0:
        print("Incorrect parameters")
    else:
        i = alist[3] / (12 * 100)
        while dif_month <= alist[2]:
            dm = (alist[1] / alist[2]) + i * (alist[1] - (alist[1] * (dif_month - 1) / alist[2]))
            dm = math.ceil(dm)
            print(f"Month {dif_month}: payment is {dm}")
            overpay += dm
            dif_month += 1
        print('')
        overpay1 = overpay - alist[1]
        print(f'Overpayment = {overpay1}')

elif alist[0] == 'annuity':
    if args.interest is None or args.type not in alist or len(alist) != 4:
        print("Incorrect parameters")
        exit()
    elif alist[1] < 0 or alist[2] < 0 or alist[3] < 0:
        print("Incorrect parameters")
    if args.payment is None:
        i = args.interest / (12 * 100)
        power = 1 + i
        annuity = args.principal * ((i * math.pow(power, args.periods)) / (math.pow(power, args.periods) - 1))
        annuity = math.ceil(annuity)
        print(f'Your annuity payment = {annuity}!')
        overpayment = args.periods * annuity - args.principal
        print('')
        print(f'Overpayment = {overpayment}')
    if args.principal is None:
        i = args.interest / (12 * 100)
        power = 1 + i
        principal = args.payment / ((i * math.pow(power, args.periods)) / (math.pow(power, args.periods) - 1))
        principal = math.ceil(principal)
        print(f'Your loan principal = {principal}!')
        overpayment = args.periods * args.payment - principal
        print('')
        print(f'Overpayment = {overpayment}')
    if args.periods is None:
        i = args.interest / (12 * 100)
        base = 1 + i
        x = args.payment / (args.payment - i * args.principal)
        n = math.log(x, base)
        n_months = math.ceil(n)
        years = 0
        over = n_months * args.payment - args.principal
        while n_months >= 12:
            years += 1
            n_months -= 12
        if n_months > 1 and years > 1:
          m = 'months'
          y = 'years'
          print(f"It will take {years} {y} and {n_months} {m} to repay this loan!")
          print('')
          print(f'Overpayment = {over}')
        elif n_months > 1 and years == 0:
            m = 'months'
            print(f"It will take {n_months} {m} to repay the loan!")
            print('')
            print(f'Overpayment = {over}')
        elif n_months == 0 and years > 1:
            y = 'years'
            print(f"It will take {years} {y} to repay the loan!")
            print('')
            print(f'Overpayment = {over}')
        elif n_months == 1 and years > 1:
            m = 'month'
            y = 'years'
            print(f"It will take {years} {y} and {n_months} {m} to repay this loan!")
            print('')
            print(f'Overpayment = {over}')
        elif n_months > 1 and years == 1:
            m = 'months'
            y = 'year'
            print(f"It will take {years} {y} and {n_months} {m} to repay this loan!")
            print('')
            print(f'Overpayment = {over}')
        elif n_months == 1 and years == 1:
            m = 'month'
            y = 'year'
            print(f"It will take {years} {y} and {n_months} {m} to repay this loan!")
            print('')
            print(f'Overpayment = {over}')

else:
    print('Incorrect parameters')
