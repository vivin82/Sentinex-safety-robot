import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to convert a binary list to a decimal number
def binary_to_decimal(binary_list):
    """Converts a binary list to a decimal number."""
    return int(''.join(map(str, binary_list)), 2)

# Function to perform the Rank-Order Clustering Technique
def rank_order_clustering(part_machine_matrix):
    """Applies Rank-Order Clustering Technique to the part-machine matrix."""
    matrix = np.array(part_machine_matrix)  # Convert to numpy array for easier manipulation
    
    # Initialize matrices to store the reordered results
    matrix_reordered_rows = matrix.copy()
    matrix_reordered_columns = matrix.copy()
    
    # Keep track of all iterations
    iteration_matrices = []
    
    # Repeat the process iteratively until convergence
    converged = False
    iteration = 1
    while not converged:
        converged = True  # Assume convergence
        
        # Step 1: Convert each row to its decimal equivalent
        row_decimals = [binary_to_decimal(row) for row in matrix_reordered_rows]
        
        # Step 2: Rank rows based on decimal values
        row_ranking = sorted(range(len(row_decimals)), key=lambda i: row_decimals[i], reverse=True)
        
        # Step 3: Reorder rows based on the rankings
        new_matrix_reordered_rows = matrix_reordered_rows[row_ranking]
        
        # Check for changes in row order
        if not np.array_equal(new_matrix_reordered_rows, matrix_reordered_rows):
            matrix_reordered_rows = new_matrix_reordered_rows
            converged = False
        
        # Step 4: Convert each column to its decimal equivalent (column-major order)
        column_decimals = [binary_to_decimal(matrix_reordered_rows[:, i]) for i in range(matrix_reordered_rows.shape[1])]
        
        # Step 5: Rank columns based on decimal values
        column_ranking = sorted(range(len(column_decimals)), key=lambda i: column_decimals[i], reverse=True)
        
        # Step 6: Reorder columns based on the rankings
        new_matrix_reordered_columns = matrix_reordered_rows[:, column_ranking]
        
        # Check for changes in column order
        if not np.array_equal(new_matrix_reordered_columns, matrix_reordered_columns):
            matrix_reordered_columns = new_matrix_reordered_columns
            converged = False
        
        # Save the matrix after each iteration for visualization
        iteration_matrices.append(matrix_reordered_columns)
        iteration += 1

    # Return the final matrix, row and column orders, and all iteration matrices
    return matrix_reordered_columns, row_ranking, column_ranking, iteration_matrices

# Function to display the results of the analysis
def display_results(final_matrix, row_order, column_order, original_matrix, iteration_matrices):
    """Displays the final group technology matrix with row and column orders."""
    
    # Display the original matrix
    print("\nOriginal Part-Machine Matrix:")
    print(np.array(original_matrix))
    
    # Display the final reordered matrix
    print("\nFinal Group Technology Matrix (Reordered):")
    print(final_matrix)
    
    # Display the row and column orderings
    print("\nRow Order (Parts):", row_order)
    print("Column Order (Machines):", column_order)
    
    # Visualize the iteration process and final result
    plot_iterations(iteration_matrices)
    
    # Final diagonal visualization of the clustering
    plot_heatmap(final_matrix, "Final Group Technology Matrix (Reordered) - Diagonal Clusters")

# Function to plot the heatmap
def plot_heatmap(matrix, title):
    """Plots a heatmap for the given matrix."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", cbar=False, linewidths=0.5)
    plt.title(title)
    plt.xlabel("Machines")
    plt.ylabel("Parts")
    plt.show()

# Function to plot the heatmap of iteration matrices
def plot_iterations(iteration_matrices):
    """Plots the heatmaps for each iteration of the clustering process."""
    for i, matrix in enumerate(iteration_matrices):
        plt.figure(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", cbar=False, linewidths=0.5)
        plt.title(f"Iteration {i+1}")
        plt.xlabel("Machines")
        plt.ylabel("Parts")
        plt.show()

# Function to get user input for the part-machine matrix
def get_user_input():
    """Gets the part-machine matrix input from the user."""
    # Get the number of parts and machines
    num_parts = int(input("Enter the number of parts: "))
    num_machines = int(input("Enter the number of machines: "))
    
    # Initialize an empty matrix
    part_machine_matrix = []
    
    # Get the part-machine relationship for each part
    print("\nEnter the part-machine relationship matrix (1 for part uses machine, 0 otherwise):")
    for i in range(num_parts):
        while True:
            row = input(f"Enter the row for part {i+1} (binary values for machines separated by space): ").split()
            if len(row) != num_machines or not all(x in ['0', '1'] for x in row):
                print(f"Invalid input. Please enter exactly {num_machines} binary values (0 or 1) for part {i+1}.")
            else:
                part_machine_matrix.append(list(map(int, row)))
                break
    
    return part_machine_matrix

# Main program
if __name__ == "__main__":
    # Get user input
    part_machine_matrix = get_user_input()

    # Run the Rank-Order Clustering Algorithm
    final_matrix, row_order, column_order, iteration_matrices = rank_order_clustering(part_machine_matrix)

    # Display the final results and visualize the process
    display_results(final_matrix, row_order, column_order, part_machine_matrix, iteration_matrices)
