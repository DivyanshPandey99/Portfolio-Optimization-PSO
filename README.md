# Portfolio Optimization by PSO Algorithm

This project demonstrates the use of Particle Swarm Optimization (PSO) algorithm to optimize an investment portfolio.

According to Wikipedia, Portfolio optimization is the process of selecting the best portfolio (asset distribution), out of the set of all portfolios being considered, according to some objective. The objective typically maximizes factors such as expected return, and minimizes costs like financial risk.

In computational science, Particle swarm optimization (PSO) is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according to simple mathematical formula over the particle's position and velocity. Each particle's movement is influenced by its local best known position, but is also guided toward the best known positions in the search-space, which are updated as better positions are found by other particles. This is expected to move the swarm toward the best solutions.

### Sharpe Ratio as Fitness Function

Sharpe Ratio is a commonly used measure to evaluate the performance of an investment portfolio. It measures the excess return of a portfolio over the risk-free rate per unit of its volatility.

The Sharpe Ratio is calculated as:

```
Sharpe Ratio = (Rp - Rf) / σp
```

where

**Rp** is the portfolio return

**Rf** is the risk-free rate of return

**σp** is the portfolio volatility (standard deviation)

The Sharpe Ratio measures the risk-adjusted return of an investment portfolio. A higher Sharpe Ratio indicates better performance, as it shows that the portfolio is generating higher returns for the level of risk taken.

In this project, the Sharpe Ratio is used as the fitness function to evaluate the performance of each particle in the PSO algorithm. The Sharpe Ratio of each particle's portfolio allocation is calculated, and the particle with the highest Sharpe Ratio is selected as the best solution.

By using the Sharpe Ratio as the fitness function, the PSO algorithm can optimize the portfolio allocation to generate the highest risk-adjusted returns. This allows investors to make better investment decisions and maximize their returns while minimizing their risks.

## Requirements

- Python 3.x

- Pandas

- Numpy

- Matplotlib

## Output

Similarity to output in research paper in reference section:

![Similarity to Research paper](https://github.com/DivyanshPandey99/Portfolio-Optimization-PSO/blob/master/Particle_Swarm_Optimization.png)

**Final output:**

![Final output](https://github.com/DivyanshPandey99/Portfolio-Optimization-PSO/blob/master/Particle_Swarm_Optimization-2.png)

## References

- [Particle swarm optimization approach to portfolio optimization - Tunchan Cura](https://staff.fmi.uvt.ro/~daniela.zaharie/ma2016/projects/applications/portfolio_optimization/PSO%2Bportfolio.pdf)

- [Portfolio Optimization using MPT in Python](https://www.analyticsvidhya.com/blog/2021/04/portfolio-optimization-using-mpt-in-python/)

