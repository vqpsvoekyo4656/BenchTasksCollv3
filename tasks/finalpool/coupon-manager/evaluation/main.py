# Evaluation script for coupon-manager
# This file evaluates the agent's work on the coupon-manager task

def evaluate(workspace_dir):
    """Evaluate the coupon-manager task implementation."""
    # Check if required files exist
    import os
    
    required_files = [
        'coupon_manager.py',
        'README.md'
    ]
    
    results = {}
    for f in required_files:
        path = os.path.join(workspace_dir, f)
        results[f] = os.path.exists(path)
    
    # Check if all required files exist
    all_exist = all(results.values())
    
    return {
        'passed': all_exist,
        'score': 1.0 if all_exist else 0.0,
        'details': results
    }
