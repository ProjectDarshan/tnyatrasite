import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches

class Vector3DGrapher:
    def __init__(self):
        self.vectors = []  # List of tuples: (name, (x, y, z), color)
        self.fig = None
        self.ax = None
        
    def add_vector(self, name, components, color=None):
        """My
        Add a vector to the graph.
        
        Parameters:
        -----------
        name : str
            Label for the vector
        components : tuple or list
            (x, y, z) components of the vector
        color : str, optional
            Color of the vector arrow
        """
        if color is None:
            # Auto-assign colors
            colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
            color = colors[len(self.vectors) % len(colors)]
        
        self.vectors.append((name, tuple(components), color))
    
    def clear_vectors(self):
        """Clear all vectors."""
        self.vectors = []
    
    def plot(self, grid_size=10, show_axes=True, show_legend=True, equal_aspect=True):
        """
        Plot all vectors in 3D space.
        
        Parameters:
        -----------
        grid_size : int
            Size of the grid to display
        show_axes : bool
            Whether to show axis lines
        show_legend : bool
            Whether to show legend
        equal_aspect : bool
            Whether to use equal aspect ratio
        """
        # Create figure
        self.fig = plt.figure(figsize=(12, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Plot each vector
        for name, (x, y, z), color in self.vectors:
            self._draw_vector(x, y, z, color, name)
            # Display vector components as text
            self.ax.text(x, y, z, f'  {name}\n  ({x:.2f}, {y:.2f}, {z:.2f})', 
                        fontsize=9, color=color)
        
        # Set axis limits
        all_coords = [coord for _, (x, y, z), _ in self.vectors for coord in [x, y, z]]
        if all_coords:
            max_coord = max(abs(c) for c in all_coords)
            max_coord = max(max_coord, grid_size / 2)
            self.ax.set_xlim([-max_coord, max_coord])
            self.ax.set_ylim([-max_coord, max_coord])
            self.ax.set_zlim([-max_coord, max_coord])
        
        # Draw coordinate axes
        if show_axes:
            self._draw_axes(grid_size)
        
        # Labels
        self.ax.set_xlabel('X Axis', fontsize=12, labelpad=10)
        self.ax.set_ylabel('Y Axis', fontsize=12, labelpad=10)
        self.ax.set_zlabel('Z Axis', fontsize=12, labelpad=10)
        self.ax.set_title('3D Vector Grapher', fontsize=14, fontweight='bold', pad=20)
        
        # Equal aspect ratio
        if equal_aspect:
            self.ax.set_box_aspect([1, 1, 1])
        
        # Legend
        if show_legend and self.vectors:
            legend_elements = [mpatches.Patch(color=color, label=f'{name}: ({x:.2f}, {y:.2f}, {z:.2f})')
                             for name, (x, y, z), color in self.vectors]
            self.ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
        
        # Grid
        self.ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def _draw_vector(self, x, y, z, color, label):
        """Draw a single vector as an arrow from origin."""
        # Draw the arrow line
        self.ax.quiver(0, 0, 0, x, y, z, color=color, arrow_length_ratio=0.15,
                      linewidth=2.5, alpha=0.8)
        
        # Calculate vector magnitude
        magnitude = np.sqrt(x**2 + y**2 + z**2)
        return magnitude
    
    def _draw_axes(self, length):
        """Draw coordinate axes."""
        # X axis (red)
        self.ax.quiver(0, 0, 0, length, 0, 0, color='red', alpha=0.3, 
                      arrow_length_ratio=0.1, linestyle='--', linewidth=1)
        # Y axis (green)
        self.ax.quiver(0, 0, 0, 0, length, 0, color='green', alpha=0.3,
                      arrow_length_ratio=0.1, linestyle='--', linewidth=1)
        # Z axis (blue)
        self.ax.quiver(0, 0, 0, 0, 0, length, color='blue', alpha=0.3,
                      arrow_length_ratio=0.1, linestyle='--', linewidth=1)
    
    def get_vector_info(self):
        """Print information about all vectors."""
        print("\n" + "="*60)
        print("Vector Information")
        print("="*60)
        for i, (name, (x, y, z), color) in enumerate(self.vectors, 1):
            magnitude = np.sqrt(x**2 + y**2 + z**2)
            print(f"\n{i}. {name}")
            print(f"   Components: ({x:.4f}, {y:.4f}, {z:.4f})")
            print(f"   Magnitude:  {magnitude:.4f}")
            if magnitude > 0:
                print(f"   Unit Vector: ({x/magnitude:.4f}, {y/magnitude:.4f}, {z/magnitude:.4f})")
        print("="*60 + "\n")


def example_usage():
    """Example usage of the 3D Vector Grapher."""
    # Create grapher instance
    grapher = Vector3DGrapher()
    
    # Add some example vectors
    grapher.add_vector("Vector 1", (3, 4, 5), color='red')
    grapher.add_vector("Vector 2", (-2, 3, -4), color='blue')
    grapher.add_vector("Vector 3", (1, 1, 1), color='green')
    
    # Show vector information
    grapher.get_vector_info()
    
    # Plot the vectors
    grapher.plot(grid_size=8, show_axes=True, show_legend=True)


def interactive_mode():
    """Interactive mode to input vectors manually."""
    grapher = Vector3DGrapher()
    
    print("\n" + "="*60)
    print("3D Vector Grapher - Interactive Mode")
    print("="*60)
    print("Enter vectors to visualize. Type 'done' when finished.")
    print("Format: name x y z [color]")
    print("Example: MyVector 3 4 5 red")
    print("="*60 + "\n")
    
    while True:
        try:
            user_input = input("Enter vector (or 'done' to plot, 'clear' to reset): ").strip()
            
            if user_input.lower() == 'done':
                break
            elif user_input.lower() == 'clear':
                grapher.clear_vectors()
                print("All vectors cleared.\n")
                continue
            elif not user_input:
                continue
            
            parts = user_input.split()
            if len(parts) < 4:
                print("Error: Need at least name and x, y, z components.")
                continue
            
            name = parts[0]
            x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            color = parts[4] if len(parts) > 4 else None
            
            grapher.add_vector(name, (x, y, z), color)
            print(f"Added vector '{name}' with components ({x}, {y}, {z})\n")
            
        except ValueError:
            print("Error: Invalid input. Please enter numbers for x, y, z components.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            return
        except Exception as e:
            print(f"Error: {e}")
    
    if grapher.vectors:
        grapher.get_vector_info()
        grapher.plot(grid_size=10, show_axes=True, show_legend=True)
    else:
        print("No vectors to plot.")


if __name__ == "__main__":
    # This will now always start the interactive mode automatically
    interactive_mode()