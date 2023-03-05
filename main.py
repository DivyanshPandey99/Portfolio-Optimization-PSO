import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



plt.figure(figsize=(10,5), num="Particle Swarm Optimization")
font = {'family':'sans-serif','color':'darkred','size':15}
font2 = {'weight':'heavy'}


def portfolio_fitness(weights, returns):
    """
    Calculates the fitness of a portfolio given the weights and returns.
    """
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    portfolio_sharpe_ratio = portfolio_return / portfolio_volatility
    return np.array([portfolio_return, portfolio_volatility, portfolio_sharpe_ratio])

def particle_swarm_optimization(returns, num_particles, max_iterations, alpha, beta):
    """
    Performs portfolio optimization using particle swarm optimization.
    """
    # Initialize particles and velocities
    particles = np.random.rand(num_particles, returns.shape[1])
    velocities = np.zeros((num_particles, returns.shape[1]))
    
    # Initialize global best
    global_best_fitness = None #Array
    global_best_weights = None #Array
    
    # Initialize 1st plot
    plt.subplot(1,2,1)
    plt.xlabel("Risk(Volatility)", fontdict=font2)
    plt.ylabel("Returns" , fontdict=font2)
    plt.title("Sharpe ratio graph", fontdict= font)
    xaxis = []
    yaxis = []
    
    # Iterate through each particle
    for i in range(num_particles):

        particles[i] = particles[i]/np.sum(particles[i])
        # Calculate particle fitness
        particle_fitness = portfolio_fitness(particles[i], returns)
        
        # Initialize particle best
        particle_best_fitness = particle_fitness
        particle_best_weights = particles[i]
        
        # Update global best
        if global_best_fitness is None or particle_best_fitness[2] > global_best_fitness[2]:
            global_best_fitness = particle_best_fitness
            global_best_weights = particle_best_weights
            
        # Iterate through iterations
        for j in range(max_iterations):
            # Update velocity
            velocities[i] = alpha * velocities[i] + beta * np.random.uniform(0, 1) * (particle_best_weights - particles[i]) + beta * np.random.uniform(0, 1) * (global_best_weights - particles[i])
            
            # Update particle position
            particles[i] = particles[i] + velocities[i]
            
            particles[i] = particles[i]/np.sum(particles[i])
            # Ensure particle weights are within bounds
            particles[i] = np.minimum(particles[i], 1)
            particles[i] = np.maximum(particles[i], 0)
            
            # Calculate particle fitness
            particle_fitness = portfolio_fitness(particles[i], returns)
            
            # Update particle best
            if particle_fitness[2] > particle_best_fitness[2]:
                particle_best_fitness = particle_fitness
                particle_best_weights = particles[i]
                
                # Update global best
                if particle_best_fitness[2] > global_best_fitness[2]:
                    global_best_fitness = particle_best_fitness
                    global_best_weights = particle_best_weights
        
            xaxis.append(particle_fitness[1])
            yaxis.append(particle_fitness[0])

            # Remove this for loop and uncomment the line plt.pause() to get one by one animation of plotting
            if(i ==  num_particles-1 and j == max_iterations-1):
                plt.scatter(xaxis,yaxis , color ='#1f77b4' ,s=10)
                #plt.pause(0.0000005) 
        
        

    return global_best_weights, global_best_fitness
    
# Example usage
returns = pd.read_csv('returns.csv')
weights, fitness = particle_swarm_optimization(returns, num_particles=100, max_iterations=100, alpha=0.1, beta=0.1)
weights = weights/np.sum(weights)

print('Optimized weights:', weights)
print('Optimized portfolio return:', fitness[0])
print('Optimized portfolio volatility:', fitness[1])
print('Optimized portfolio Sharpe ratio:', fitness[2])

# Plot best sharpe ratio on sharpe ratio graph
plt.scatter(fitness[1],fitness[0],marker="*",s = 50, color = 'red')
#plt.pause(0.0000005)

#Get titles of column , i.e. , company names
column_headers = list(returns.columns.values)


plt.subplot(1,2,2)
plt.title("Optimal Portfolio Distribution" , fontdict=font)
plt.xlabel("Stocks", fontdict=font2)
plt.ylabel("Weights" , fontdict= font2)
plt.bar(np.array(column_headers),weights)
plt.show()
