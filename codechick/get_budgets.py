# https://codechick.io/challenges/397


def get_budgets(lst):
    total_sum = 0
    for data in lst:
        total_sum += data['budget']
    return total_sum
