# 🚀 Quick Start Guide

Get up and running with Expense Tracker in 2 minutes!

## Step 1: Run the Application

```bash
python3 expense_tracker.py
```

## Step 2: Try with Sample Data

To test with pre-loaded sample data:

```bash
# Copy sample data to active data file
cp data/sample_expenses.json data/expenses.json

# Run the application
python3 expense_tracker.py
```

Now you can:

- Press `2` to view all sample expenses
- Press `3` to see total expenses
- Press `6` to see category breakdown

## Step 3: Add Your First Expense

1. Run the application
2. Press `1` to add an expense
3. Press Enter to use today's date
4. Enter category: `food`
5. Enter amount: `25.50`
6. Enter description: `Lunch`

## Common Commands

### View Everything

```
Choice: 2
```

### See Monthly Breakdown

```
Choice: 4
Press Enter (to see all months)
```

### Filter by Category

```
Choice: 5
Enter: food
```

### Export Report

```
Choice: 7
```

Report saved to `data/expense_summary.txt`

## Tips

- **Date Format**: Always use YYYY-MM-DD (e.g., 2024-01-15)
- **Categories**: Use consistent names (food, transport, utilities, entertainment)
- **Quick Date**: Press Enter when adding expense to use today's date
- **Data Location**: All data saved in `data/expenses.json`

## Example Session

```
$ python3 expense_tracker.py

1. Add Expense
Enter your choice: 1

Enter date or press Enter for today: [Enter]
Enter category: food
Enter amount: $35.50
Enter description: Dinner at restaurant
✓ Expense added successfully

Enter your choice: 3
Total Expenses: $35.50
```

That's it! You're ready to track your expenses. 💰
