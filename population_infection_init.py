
class Population:
    swiss_pop = 8500000 #Swiss population
    infected = 1000
    dead = 11
    recovered = 4
    #It is assumed that a recovered persone can not be infected anymore.
    suceptibles = swiss_pop - infected-dead-recovered
    #we assume there are no birth during the epidemie
    N = suceptibles + infected + recovered - dead 

class Disease:
    #in average in takes 14 days for a person to heal
    rate_of_recovery = 1/14 

    #In avg. it takes 1 hour for someone to get sick.
    rate_of_infectiom = 12

    #Based on worldometer, the mortality is around 7 %
    death_prob = 0.07