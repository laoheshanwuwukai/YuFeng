#include <iostream>
#include <nlopt.hpp>

/*
object function:
  f(x,y) = (x-1)^2+ (y-2)^2

constrain:
  x^2 + y^2 <=1
 */

double objective(const std::vector<double> &x, std::vector<double> &grad,
                 void *data) {
  if (!grad.empty()) {
    grad[0] = 2 * (x[0] - 1);
    grad[1] = 2 * (x[1] - 2);
  }
  return (x[0] - 1) * (x[0] - 1) + (x[1] - 2) * (x[1] - 2);
}

double constraint(const std::vector<double> &x, std::vector<double> &grad,
                  void *data) {
  if (!grad.empty()) {
    grad[0] = 2 * x[0];
    grad[1] = 2 * x[1];
  }
  return x[0] * x[0] + x[1] * x[1] - 1; // 小于等于0
}

int main() {
  nlopt::opt opt(nlopt::LD_MMA, 2);
  opt.set_min_objective(objective, nullptr);

  opt.add_inequality_constraint(constraint, nullptr, 1e-8);
  opt.set_xtol_rel(1e-4);

  std::vector<double> x = {0.5, 0.5}; // 初值
  double minf;
  nlopt::result result = opt.optimize(x, minf);

  std::cout << "Minimum at (" << x[0] << ", " << x[1] << ") with value " << minf
            << std::endl;

  double x_ratio = x[0] / x[1];
  double y_ratio = 1. / 2;
  std::cout << "result x_ratio:" << x_ratio << std::endl;
  std::cout << "result y_ratio:" << y_ratio << std::endl;
}

