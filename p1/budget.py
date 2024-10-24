company_name = str(input("Company Name: ")) 
daily_revenue = int(input("Daily Revenue: "))
daily_expenses = int(input("Daily Expenses: "))
daily_profit = daily_revenue - daily_expenses
daily_profit_margin = daily_profit/daily_revenue
made_profit = False

if daily_profit_margin > 0.75:
    lucrative = True
else:
    lucrative = False

if daily_revenue > daily_expenses:
    made_profit = True
    
if lucrative:
    print(f"{company_name} was lucrative today" , end = '\n')
elif made_profit:
    print(f"{company_name} made a profit today" , end = '\n')
else:
    print(f"{company_name} did not make a profit today" , end = '\n')
    
print(f"Daily Revenue: £{daily_revenue}" , end = '\n')
print(f"Daily Expenses: £{daily_expenses}" , end = '\n')
print(f"Daily Profit: £{daily_profit}" , end = '\n')
print(f"Daily Profit Margin: {daily_profit_margin}")
