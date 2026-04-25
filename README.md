# 3D Vector Grapher

A Python application for visualizing 3D vectors in an interactive 3D space. This tool allows you to plot multiple vectors as arrows from the origin, view their components, magnitudes, and unit vectors.

## Features

- **3D Vector Visualization**: Display vectors as arrows in 3D space
- **Multiple Vectors**: Plot and compare multiple vectors simultaneously
- **Vector Information**: Automatically calculates and displays:
  - Vector components (x, y, z)
  - Magnitude
  - Unit vector
- **Interactive Mode**: Input vectors dynamically through the command line
- **Color Coding**: Assign colors to different vectors for easy identification
- **Coordinate Axes**: Visual reference axes for orientation

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy matplotlib
```

## Usage

### Basic Example

Run the default example:
```bash
python main.py
```

This will display three example vectors in a 3D plot.

### Interactive Mode

For interactive input:
```bash
python main.py --interactive
```

In interactive mode, you can:
- Add vectors: `name x y z [color]`
  - Example: `MyVector 3 4 5 red`
- Clear all vectors: `clear`
- Finish and plot: `done`

### Using the API

You can also use the `Vector3DGrapher` class in your own code:

```python
from main import Vector3DGrapher

# Create a grapher instance
grapher = Vector3DGrapher()

# Add vectors
grapher.add_vector("Vector 1", (3, 4, 5), color='red')
grapher.add_vector("Vector 2", (-2, 3, -4), color='blue')

# Display vector information
grapher.get_vector_info()

# Plot the vectors
grapher.plot(grid_size=10, show_axes=True, show_legend=True)
```

## Examples

### Example 1: Basic Unit Vectors
```python
grapher = Vector3DGrapher()
grapher.add_vector("i-hat", (1, 0, 0), color='red')
grapher.add_vector("j-hat", (0, 1, 0), color='green')
grapher.add_vector("k-hat", (0, 0, 1), color='blue')
grapher.plot()
```

### Example 2: Vector Operations Visualization
```python
grapher = Vector3DGrapher()
v1 = (3, 4, 5)
v2 = (1, 2, 3)
v_sum = (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

grapher.add_vector("Vector 1", v1, color='red')
grapher.add_vector("Vector 2", v2, color='blue')
grapher.add_vector("Sum", v_sum, color='green')
grapher.plot()
```

## Controls

- **Rotate**: Click and drag to rotate the 3D plot
- **Zoom**: Use the scroll wheel to zoom in/out
- **Pan**: Right-click and drag to pan

## License

This project is open source and available for use.
