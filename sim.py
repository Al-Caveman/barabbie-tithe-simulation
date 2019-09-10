SAVINGS = 33879 # median saving of white ppl in u.s.a. in 2016
INCOME = 68145 # median household income of white ppl in u.s.a. in 2017
EXPENSES = 62031 # average expenses for whites in usa in 2017
CHARITY_RATE = 0.1 # 10% -- ask ur local church's pedo for further info.
YEARS = 1000 # we shall simulate barabbie for 50 years.

def sim(savings, income, expenses, charity_rate, charity_on_savings, years):
    print('year    savings')
    current_savings = SAVINGS
    total_tithes = 0
    for year in range(0, YEARS):
        current_tithe = income*charity_rate
        if charity_on_savings:
            current_tithe += current_savings*charity_rate
        current_savings += income - expenses - current_tithe
        print('{:<8}{}'.format(year, current_savings))
        if current_savings < 0:
            break
    print('')

print('simulating barabbas tithes')
sim(SAVINGS, INCOME, EXPENSES, CHARITY_RATE, True, YEARS)

print('simulating common tithes')
sim(SAVINGS, INCOME, EXPENSES, CHARITY_RATE, False, YEARS)

print('simulating zakat')
sim(SAVINGS, INCOME, EXPENSES, 0.025, True, YEARS)
