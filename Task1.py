import heapq

def min_cost_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

        print(
            f"Combining {first} and {second} cables with {cost} costs. Total costs: {total_cost}"
        )
        print(f"Current state of the heap: {cables}")


    return total_cost


cables = [4,7,2,8,6]
print(f'Minimum cost to connect all cables: {min_cost_cables(cables)}')







