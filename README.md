# Probability Calculator

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Probability Calculator application, follow the instructions in the Setup section below.

## Project Structure

- `prob_calculator.py`: Contains the implementation of the `Hat` class and the `experiment` function.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/probability-calc-fcc-scicomp-py-cert.git
   cd probability-calculator-fcc-scicomp-py-cert
   ```

2. Run the Probability Calculator script:
   ```bash
   python3 main.py
   ```

## Probability Calculator

### Functionality

The Probability Calculator allows you to simulate drawing balls from a hat and calculate the probability of drawing a specific combination of balls over a number of experiments.

### Hat Class

#### Methods

- `__init__(self, **balls)`: Initializes a new hat with a given number of balls of different colors.
- `draw(self, num)`: Draws a specified number of balls from the hat. If the number of balls to draw exceeds the available balls, it draws as many as possible.

### Experiment Function

The `experiment` function simulates the process of drawing balls from the hat multiple times and calculates the probability of drawing a specific combination of balls.

#### Parameters

- `hat`: An instance of the `Hat` class.
- `expected_balls`: A dictionary indicating the expected number of each color of ball to be drawn.
- `num_balls_drawn`: The number of balls to draw in each experiment.
- `num_experiments`: The number of experiments to perform.

#### Returns

- The probability of drawing the expected combination of balls at least once in the specified number of experiments.

### Practical Use Case

The Probability Calculator can be used to model and solve probability problems, especially those involving random sampling without replacement.

### Benefits

- **Simulation of Random Events:** Provides a way to simulate and understand random events.
- **Probability Calculation:** Helps in calculating the probability of complex events.
- **Python Standard Library:** Utilizes Python’s built-in libraries for random sampling and deep copying.

## How to Use

1. Create an instance of the `Hat` class with the desired number of balls of different colors.
2. Use the `experiment` function to simulate the drawing process and calculate probabilities.

### Example Usage

```python
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
```

### Example Output

```plaintext
Probability: 0.17066666666666666
...............
----------------------------------------------------------------------
Ran 3 tests in 0.028s

OK
```

### Additional Information

- **Deep Copy:** Ensures the original hat is not modified during the experiments.
- **Random Sampling:** Uses random sampling to simulate the drawing process realistically.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
