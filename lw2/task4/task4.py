from abc import ABC, abstractmethod
import numpy as np

def fibo(n):
    nums = []
    a, b = 0, 1
    for i in range(n):
        nums.append(a)
        a, b = b, a + b
    return nums 
class NumberGenerationStrategy(ABC):
   @abstractmethod
   def generate_numbers(self,*args,**kwargs):
      pass

class pPercentileCalculationStrategy(ABC):
   @abstractmethod
   def find_pth_percentile(self,numbers,percentile):
      return 

class DistributionTester():
   def __init__(self,generating_strategy , p_percentile_calculation):
      self._generating_strategy = generating_strategy 
      self._p_percentile_calculation = p_percentile_calculation
   def test_number_distribution(self,*args,**kwargs):
      numbers = self._generating_strategy.generate_numbers(*args,**kwargs)
      numbers.sort()
      print(f"Numbers : {numbers}")
      for p in range (10,100,10):
         print(f"Numbers {p}th percentile : {self._p_percentile_calculation.find_pth_percentile(numbers,p)}")
   
class SequentialNumberGenerationStrategy(NumberGenerationStrategy):
   def generate_numbers(self,lower_bound,upper_bound,step):
      return [x for x in range(lower_bound, upper_bound + 1, step)]
   
class RandomNumberGenerationStrategy(NumberGenerationStrategy):
   def generate_numbers(self,mean,std,num_elements):
      return np.random.normal(mean,std,num_elements)
   
class FibonacciNumberGenerationStrategy(NumberGenerationStrategy): 
    def generate_numbers(self, n_elements):
        return fibo(n_elements)

class LinearInterpolation(pPercentileCalculationStrategy):
   def find_pth_percentile(self, numbers, percentile):
      N = len(numbers)  
      for i in range(N-1):
         p_v_i = 100*(i-0.5) / N
         if p_v_i < percentile:
            p_v_i2 = 100*((i+1)-0.5) / N    
            if p_v_i2 >= percentile:    
               return numbers[i] + N*(percentile - p_v_i)/100 * (numbers[i+1] - numbers[i])
   
class NearestRankMethod(pPercentileCalculationStrategy):
   def find_pth_percentile(self, numbers, percentile):
      return numbers[int(percentile * len(numbers) / 100 +0.5)]

def main():
   
   sequential_numbers_linear_interpolation = DistributionTester(SequentialNumberGenerationStrategy(),LinearInterpolation())
   sequential_numbers_linear_interpolation.test_number_distribution(1,100,1)
   print("------------------------------------------------------------------------------------------------------------------")
   sequential_numbers_nearest_rank_method = DistributionTester(SequentialNumberGenerationStrategy(),NearestRankMethod())
   sequential_numbers_nearest_rank_method.test_number_distribution(1,100,1)
   print("------------------------------------------------------------------------------------------------------------------")
   
   random_numbers_linear_interpolation = DistributionTester(RandomNumberGenerationStrategy(),LinearInterpolation())
   random_numbers_linear_interpolation.test_number_distribution(0,1,100) 
   random_numbers_nearest_rank_method = DistributionTester(RandomNumberGenerationStrategy(),NearestRankMethod())
   random_numbers_nearest_rank_method.test_number_distribution(0,1,100) 
   print("------------------------------------------------------------------------------------------------------------------")
   
   fibonnaci_numbers_linear_interpolation = DistributionTester(FibonacciNumberGenerationStrategy(),LinearInterpolation())
   fibonnaci_numbers_linear_interpolation.test_number_distribution(20)
   fibonnaci_numbers_nearest_rank_method = DistributionTester(FibonacciNumberGenerationStrategy(),NearestRankMethod())
   fibonnaci_numbers_nearest_rank_method.test_number_distribution(20)
   print("------------------------------------------------------------------------------------------------------------------")
   
   return

if __name__ == '__main__':
   main()