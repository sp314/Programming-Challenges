n_saplings = int(input())
saplingsList = list(map(int, input().split()))
saplingsList.sort(reverse= True)

max_to_maturity = 0
for n in range(n_saplings):
    to_maturity = (saplingsList[n] + n + 1)
    if(to_maturity > max_to_maturity):
        max_to_maturity = to_maturity

print(max_to_maturity + 1)






