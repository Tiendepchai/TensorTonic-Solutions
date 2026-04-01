import numpy as np

def expected_value_discrete(x, p):
    x = np.asarray(x)
    p = np.asarray(p)
    
    # Kiểm tra xem tổng xác suất có xấp xỉ bằng 1 hay không
    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("Tổng các xác suất trong p phải bằng 1.")
        
    return np.sum(x * p)