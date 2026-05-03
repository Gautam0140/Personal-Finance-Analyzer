def generate_insights(df):
    insights = []
    total_spent = abs(df[df['amount'] < 0]['amount'].sum())
    food = abs(df[df['category']=="Food"]['amount'].sum())
    if total_spent > 0:
        perc = (food / total_spent)*100
        insights.append(f"Food spending is {perc:.1f}% of total")
        if perc > 30:
            insights.append("High dependency on food delivery")
    if total_spent > 20000:
        insights.append("High monthly spending detected")
    return insights
