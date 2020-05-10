mealCost=eval(input())
tipPercent=eval(input())
taxPercent=eval(input())
tip=mealCost*(tipPercent/100)
tax=mealCost*(taxPercent/100)
totalCost=mealCost+tip+tax
print(round(totalCost))
