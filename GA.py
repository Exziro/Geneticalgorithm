import random
import math

#initialization the chrome
def specise_origin(population_size, chrome_length):
    population = [[]]#save the list, chrome and gene
    for i in range(population_size):
        temporary = []
        for j in range(chrome_length):
            temporary.append(random.randint(0,1))
            #random get a chrome binary
        population.append(temporary)
        #save the chrom in the species
    return population[1:]

#encode
def translation(population,chrome_length):
    temporary = []
    for i in range(len(population)):
        total = 0
        for j in range(chrome_length):
            total += population[i][j]*(math.pow(2,j))#decimal to binary
        temporary.append(total)
    return temporary

#fitness fuction
def function(population, chrome_length, max_value):
    temporary = []
    function1 = []
    temporary = translation(population, chrome_length)
    for i in range(len(temporary)):
        x = temporary[i]*max_value/(math.pow(2,chrome_length)-1)
        #indecode
        function1.append(2*math.sin(x)+math.cos(x))

    return function1

#chose and adjustment the fitness result
#remove non-negative numbers
def fitness(function1):
    fitness1 = []
    min_fiteness = mf = 0
    for i in range(len(function1)):
        if(function1[i]+mf > 0):
            temporary = mf + function1[i]
        else:
            temporary = 0
        #if the fitness is zero return 0 
        fitness1.append = (temporary)
    return fitness1

#add all of the fitness function 
def sum(fitness1):
    total = 0
    for i in range(len(fitness1)):
        total += fitness1[i]
    return total

#comput the add fitness
def cumsum(fitness1):
    for i in range (len(fitness1)-2,-1,-1):
        #range(start, stop, [step])
        #reverse counting
        total = 0
        j = 0
        while(j <= i):
            total += fitness1[j]
            j += 1
        fitness1[i] = total
        fitness1[len(fitness1) - 1] = 1

#chose the fit individual
def selection(population, fitness1):
    pop = [] # this is a bug 原文中没有该参数，猜测是调用
    new_fitness = []
    total_fitness = sum(fitness1)
    for i in range(len(fitness1)):
        new_fitness.append(fitness1[i]/total_fitness)

    cumsum(new_fitness)
    ms =[]
    population_length = pop_len = len(population)

    for i in range(pop_len):
        ms.append(random.random())
    ms.sort()

    fitin = 0
    newin = 0
    new_population = new_pop = population
    #roulette algorithm
    while newin < pop_len:
        if(ms[newin] < new_fitness[fitin]):
            new_pop[newin] = pop[fitin]
            newin += 1
        else:
            fitin += 1 
    population = new_pop

