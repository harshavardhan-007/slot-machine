import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "🚀":2,
    "💲":4,
    "💗":6,
    "🍒":8
}

symbol_value={
    "🚀":2,
    "💲":2,
    "💗":2,
    "🍒":2
}

def check_winnings(columns,lines,bets,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bets
            winning_lines.append(line+1)
            
    return winnings,winning_lines
    

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
                print()
    
             

def deposit():
    while True:
        amount=input("How much you would like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than zero")
        else:
            print("Enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines=input(f"Enter no.of lines to bet on 1-{MAX_LINES}?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print(f"Amount must be between 1-{MAX_LINES}")
        else:
            print("Enter a number")
    return lines

def get_bet():
    while True:
        amount=input("What would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a number")
    return amount

def spin(balance):
     line =get_number_of_lines()
     while True:
        bet=get_bet()
        totalbet=bet*line
        if totalbet>balance:
            print(f"You do not have enough balance,your current balance is: {balance}")
        else:
            break
     print(f"You are betting ${bet} on {line} lines. Total bet is equal to: ${totalbet}")
     slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
     print_slot_machine(slots)
     winnings,winning_lines=check_winnings(slots,line,bet,symbol_value)
     print(f"You won ${winnings}.")
     print(f"You won on lines:",*winning_lines)
     return winnings-totalbet

def main():
    balance = deposit()
    while True:
       print(f"Current balance is ${balance}")
       answer=input("Enter to spin or q to quit the game:")
       if answer == "q":
           break
       balance+=spin(balance)

        
    
    
main()
