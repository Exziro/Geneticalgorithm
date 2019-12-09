import random
import math
import matplotlib.pyplot as plt

class GA(object):
    def __init__(self, population_size, chrome_length, max_value, pc, pm):
        self.population_size = population_size
        self.chrome_length = chrome_length
        self.max_value = max_value
        self.pc = pc
        self.pm = pm
    #initialization the chrome



    def specise_origin(self):
        population = [[]]#save the list, chrome and gene
        for i in range(self.population_size):
            temporary = []
            for j in range(self.chrome_length):
                temporary.append(random.randint(0,1))
            #random get a chrome binary
            population.append(temporary)
        print("1")
        #save the chrom in the species
        return population[1:]

    #   code encode
    def translation(self, population):
        temporary = []
        for i in range(len(population)):
            total = 0
            for j in range(self.chrome_length):
                total += population[i][j]*(math.pow(2,j))#decimal to binary
            temporary.append(total)
        print("2")
        return temporary

    #fitness fuction
    def function(self, population):
        temporary = []
        function1 = []
        temporary = self.translation(population)
        for i in range(len(temporary)):
            x = temporary[i]*max_value/(math.pow(2,chrome_length)-1)
        #indecode
            function1.append(2*math.sin(x)+math.cos(x))
        print("3")
        return function1

    #chose and adjustment the fitness result
    #remove non-negative numbers
    def fitness(self, function1):
        fitness_value = []
        num = len(function1)
       # min_fiteness = mf = 0
        for i in range(num):
            if(function1[i] > 0):
                temporary = function1[i]
            else:
                temporary = 0.0
        #if the fitness is zero return 0 
            fitness_value.append = (temporary)
        print("4")
        return fitness_value


    #add all of the fitness function 
    def sum(self, fitness_value):
        total = 0
        for i in range(len(fitness_value)):
            total += fitness_value[i]
        print("5")
        return total

    #comput the add fitness
    def cumsum(self, fitness1):
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
        print("6")


    #chose the fit individual
    def selection(self, population, fitness_value):
        #pop = [] # this is a bug 原文中没有该参数，猜测是调用
        new_fitness = []
        total_fitness = sum(fitness_value)
        for i in range(len(fitness_value)):
            new_fitness.append(fitness_value[i]/total_fitness)

        self.cumsum(new_fitness)
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
                new_pop[newin] = population[fitin]
                newin += 1
            else:
                fitin += 1 
        population = new_pop
        print("7")
    #crossover 
    def crossover(self, population):#pc can chosed the single point crossing or multi-point cross
        pop_len = len(population)
        #population lenth
        for i in range(pop_len - 1):
            cpoint = random.randint(0, len(population[0]))
            #get the random point
            temporary1 = []
            temporary2 = []
            #save separetely chrom
            temporary1.extend(population[i][0,cpoint])
            temporary1.extend(population[i+1][cpoint:len(population[i])])
            #save the i th chrom 0~cpoint gene 
            #and then save the i+1 th chrom cpoint to the i gene add the temporary2 after
            temporary2.extend(population[i][0:cpoint])
            temporary2.extend(population[i][cpoint:len(population[i])])
            #using the t
            population[i] = temporary1
            population[i+1] = temporary2 
        print("8")
    #mutation
    def mutation(self,population,pm):#pm is mutation point
        px = len(population)
        py = len(population[0])

        for i in range(px):
            if(random.random()<self.pm):
                mpoint = random.randint(0, py-1)
                if (population[i][mpoint] == 1):
                    population[i][mpoint] = 0
                else:
                    population[i][mpoint] = 1
        print("9")

    def b2d(self, best_individual):
        total = 0
        b = len(best_individual)
        for i in range (len(b)):
            total = total + best_individual[i]*math.pow(2,i)

        total = total*self.max_value/(math.pow(2, self.chrome_length)-1)
        print("10")
        return total

    def best(self, population, fitness_value):
        px = len(population)
        bestindividual = []
        bestfitness = fitness_value[0]
        for i in range(1,px):

            if(fitness_value[i]>bestfitness):
                bestfitness = fitness_value[i]
                bestindividual = population[i]
        print("11")
        return [bestindividual, bestfitness]
    def plot(self, results):
        X = []
        Y = []
        for i in range(500):
            X.append(i)
            Y.append(results[i][0])

        plt.plot(X, Y)
        plt.show()
        print("12")
    def main(self):
        results = [[]]
        fitness_value = []
        fitmean = []

        population = pop = self.specise_origin()
        for i in range (500):
            function_value = self.fitness(population)
            fitness_value = self.fitness(function_value)

        best_individual, best_fitness = self.best(population, fitness_value)
        results.append([best_fitness, self.b2d(best_individual)])
        self.selection(population, fitness_value)
        self.crossover(population)
        results = results[1:]
        results.sort()
        self.plot(results)
        print("results")

#define part
if __name__ == ' main ':

    population_size = 500
    max_value = 10
    chrome_length = 10
    pc = 0.6
    pm = 0.01

    #result = [[]]
    #fitness1 = []
    #fitmean = []
    #population = pop = specise_origin(population_sizem, chrome_length,  max_value, pc, pm)
    
    
    ga = GA(population_size, chrome_length, max_value, pc, pm)
    ga.main()