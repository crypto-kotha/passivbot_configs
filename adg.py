def calculate_compound_growth(principal, daily_rate, days):
    balance = principal
    for _ in range(days):
        balance += balance * daily_rate
    return balance

initial_amount = 1000  # Initial principal amount
daily_rate = 0.0025  # Daily growth rate (0.25% as a decimal)
num_days = 365       # Number of days

final_balance = calculate_compound_growth(initial_amount, daily_rate, num_days)
percentage_gain = ((final_balance - initial_amount) / initial_amount) * 100

print(f"Final Balance after {num_days} days: ${final_balance:.2f}")
print(f"Percentage Gain: {percentage_gain:.2f}%")
