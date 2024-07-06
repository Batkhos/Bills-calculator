def add_expense(expense,amount,desc):
    expense.append({'amount':amount,'desc':desc})
    print(f'add expense of {desc} for {amount}$ for')

def balance(money):
    sum = 0
    for x in money:
        sum += x['amount']
    return sum

def expense_cul(expense,budget):
    return budget - balance(expense)

def details_balance(expense,budget):
    print(f'the budget was in your account : {budget}$')
    for x in expense:
        print(f'the amount of expense is : {x['amount']}$ in {x['desc']}')
    print(f'the remain amout in account is : {expense_cul(expense,budget)}$')

def main():
    all_budget = float(input('enter your budget you have : '))
    budget = all_budget
    expense= []
    while True:
        print("chose one of the follow choices bellow !")
        print('1-add new expense ')
        print('2-show the balance details')
        print('3-exit')
        choice = input('put the choice?:  ')
        if choice == '1' :
            amount=int(input('enter the amount ofthe expense : '))
            desc = input('the name of the expense: ')
            add_expense(expense,amount,desc)
        elif choice == '2':
            details_balance(expense,budget)
        elif choice == '3':
            break
        else:
            print('this choice invalid, try this choice list bellow')
main()
