import numpy as np

def page_rank(matrix, d=0.85, max_iter=100, tol=1.0e-6):
    """
    Compute the PageRank vector.
    
    Parameters:
        matrix (np.ndarray): The adjacency matrix of the graph (N x N).
        d (float): Damping factor (default=0.85).
        max_iter (int): Maximum number of iterations (default=100).
        tol (float): Tolerance to check for convergence (default=1.0e-6).
    
    Returns:
        np.ndarray: PageRank vector (N x 1).
    """
    N = matrix.shape[0]
    
    # Ensure the matrix is stochastic
    matrix = matrix / matrix.sum(axis=0, keepdims=True)
    
    # Initialize PageRank vector
    rank = np.ones(N) / N
    
    for _ in range(max_iter):
        new_rank = (1 - d) / N + d * matrix.dot(rank)
        
        # Check for convergence
        if np.linalg.norm(new_rank - rank, ord=1) < tol:
            return new_rank
        
        rank = new_rank
    
    return rank

# Example Usage
if __name__ == "__main__":
    # Adjacency matrix example (N x N)
    adjacency_matrix = np.array([[0, 0, 1, 0],
                                 [1, 0, 0, 1],
                                 [0, 1, 0, 0],
                                 [1, 1, 1, 0]])
    
    # Calculate PageRank
    page_rank_vector = page_rank(adjacency_matrix)
    print("PageRank:", page_rank_vector)
