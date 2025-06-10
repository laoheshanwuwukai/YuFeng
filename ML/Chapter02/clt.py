
# In probability theory, the central limit theorem (CLT) states that,
# under appropriate conditions, the distribution of a normalized version
# of the sample mean converges to a standard normal distribution.
# This holds even if the original variables themselves are not normally distributed.
# There are several versions of the CLT, each applying in the context of different conditions.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 模拟抛骰子：每次抛掷结果在 [1, 6] 之间
dice_outcomes = [1, 2, 3, 4, 5, 6]
population = np.random.choice(dice_outcomes, size=100000, replace=True)

# 模拟：从总体中抽取100个样本，重复10000次，记录样本均值
sample_size = 100
num_simulations = 10000
sample_means = []

for _ in range(num_simulations):
    sample = np.random.choice(population, size=sample_size, replace=False)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# 计算总体均值与样本均值分布的95%置信区间
mean = np.mean(sample_means)
std = np.std(sample_means)
ci_low = mean - 1.96 * std
ci_high = mean + 1.96 * std

# 可视化样本均值分布与置信区间
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=50, density=True,
         alpha=0.6, color='skyblue', edgecolor='black')

# 正态分布拟合曲线
x = np.linspace(min(sample_means), max(sample_means), 1000)
plt.plot(x, norm.pdf(x, mean, std), 'r--', label='Normal Approximation')

# 标注置信区间
plt.axvline(ci_low, color='green', linestyle='--',
            label=f'95% CI: [{ci_low:.2f}, {ci_high:.2f}]')
plt.axvline(ci_high, color='green', linestyle='--')
plt.axvline(mean, color='red', linestyle='-', label=f'Mean ≈ {mean:.2f}')

plt.title('Sampling Distribution of Sample Mean (CLT Demonstration)')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
