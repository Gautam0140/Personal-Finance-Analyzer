def calculate_health_score(df):
    income = df[df['amount'] > 0]['amount'].sum()
    expense = abs(df[df['amount'] < 0]['amount'].sum())
    if income == 0:
        return 0
    savings_rate = (income - expense) / income
    score = 50 + (savings_rate * 50)
    return max(0, min(100, round(score,2)))
