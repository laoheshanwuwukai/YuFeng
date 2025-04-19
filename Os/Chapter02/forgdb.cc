
// debug_demo.cpp
#include <iostream>
#include <vector>

using namespace std;

int factorial(int n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

void print_vector(const vector<int> &vec) {
  for (int i = 0; i <= vec.size(); i++) { // 这里有越界错误
    cout << vec[i] << " ";
  }
  cout << endl;
}

int main() {
  int x = 5;
  int y = 0;

  cout << "Calculating factorial of " << x << endl;
  int result = factorial(x);
  cout << "Factorial: " << result << endl;

  vector<int> numbers = {1, 2, 3, 4, 5};
  print_vector(numbers);

  int z = x / y; // 这里会导致除以零错误
  cout << "z = " << z << endl;

  return 0;
}
