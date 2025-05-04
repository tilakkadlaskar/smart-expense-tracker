import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from add_expense import add_expense

# Test case 1: Add a valid expense
add_expense(50.75, 'Food', '2025-05-04')

