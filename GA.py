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
    temporary[]
    for i in range(len(population)):
        total = 0
        for j in range(chrome_length):
            total += population[i][j]*(math.pow(2,j))#decimal to binary
        temporary.append(total)
    return temporary

#fitness fuction
def function(population, chrome_length, max_value):
    temporary[]
    function[]
    temporary = translation(population, chrome_length)
    for i in range(len(temporary)):
        x = temporary[i]*max_value/(math.pow(2,chrome_length)-1)
        #indecode
        function1.append(2*math.sin(x)+math.cos(x))

    return function1

