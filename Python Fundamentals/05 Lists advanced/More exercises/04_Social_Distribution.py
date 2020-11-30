population = input().split(", ")
min_wealth = int(input())

population = [int(el) for el in population]

for i in range(len(population)):
    if population[i] < min_wealth:
        max_p = population.index(max(population))
        min_p = population.index(min(population))
        if max(population) - min_wealth >= min_wealth - min(population):
            population[max_p] -= min_wealth - population[min_p]
            population[min_p] = min_wealth


if min(population)<min_wealth:
    print("No equal distribution possible")

else:
    print(population)
