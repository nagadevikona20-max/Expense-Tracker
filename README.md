# 💰 Expense Tracker

A professional CLI-based expense tracking application built with Python. Track your daily expenses, analyze spending patterns, and generate detailed reports.

## ✨ Features

- **Add Expenses**: Record daily expenses with date, category, amount, and description
- **View All Expenses**: Display all recorded expenses in a formatted table
- **Calculate Totals**: Get instant total of all expenses
- **Monthly Summary**: View expense breakdown by month
- **Category Filtering**: Filter expenses by specific categories
- **Category Analysis**: See spending distribution across categories with percentages
- **Export Reports**: Generate detailed summary reports in text format
- **Persistent Storage**: All data saved automatically in JSON format
- **Input Validation**: Robust validation for dates, amounts, and required fields

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd expense-tracker
```

2. Create and activate virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Run the application:

```bash
python3 expense_tracker.py
```

## 📖 Usage

### Main Menu

When you run the application, you'll see the main menu:

```
==================================================
EXPENSE TRACKER
==================================================
1. Add Expense
2. View All Expenses
3. Calculate Total Expenses
4. Monthly Summary
5. Filter by Category
6. Category-wise Summary
7. Export Summary Report
8. Exit
==================================================
```

### Adding an Expense

1. Select option `1` from the main menu
2. Enter the date (YYYY-MM-DD format) or press Enter for today's date
3. Enter a category (e.g., food, transport, utilities, entertainment)
4. Enter the amount (numeric value)
5. Enter a description

Example:

```
Enter date (YYYY-MM-DD) or press Enter for today: 2024-01-15
Enter category (e.g., food, transport, utilities): food
Enter amount: $45.50
Enter description: Grocery shopping at Whole Foods
✓ Expense added successfully (ID: 1)
```

### Viewing Expenses

Select option `2` to view all expenses in a formatted table:

```
================================================================================
ID    Date         Category        Amount     Description
================================================================================
1     2024-01-15   food            $45.50     Grocery shopping at Whole Foods
2     2024-01-16   transport       $12.00     Uber to office
================================================================================
```

### Monthly Summary

Select option `4` and either:

- Press Enter to see summary for all months
- Enter a specific month (YYYY-MM) to see that month's summary

### Category Filtering

Select option `5` and enter a category name to see all expenses in that category with a subtotal.

### Category-wise Summary

Select option `6` to see spending breakdown by category with percentages:

```
==================================================
Category-wise Summary
==================================================
Category             Total           Percentage
==================================================
Food                 $245.50         45.2%
Transport            $120.00         22.1%
Utilities            $178.00         32.7%
==================================================
Grand Total          $543.50
```

### Exporting Reports

Select option `7` to generate a comprehensive summary report saved to `data/expense_summary.txt`.

## 📁 Project Structure

```
expense-tracker/
│
├── expense_tracker.py      # Main application file
├── README.md              # This file
├── requirements.txt       # Python dependencies (if any)
├── data/                  # Data directory (auto-created)
│   ├── expenses.json      # Expense data storage
│   ├── sample_expenses.json  # Sample data for testing
│   └── expense_summary.txt   # Exported reports
└── venv/                  # Virtual environment (optional)
```

## 💾 Data Storage

- Expenses are stored in `data/expenses.json` in JSON format
- Data is automatically loaded when the program starts
- All changes are saved immediately after each operation
- The data directory is created automatically if it doesn't exist

## 🎯 Input Validation

The application includes robust input validation:

- **Date**: Must be in YYYY-MM-DD format
- **Amount**: Must be a positive numeric value
- **Category**: Cannot be empty
- **Description**: Optional (defaults to "No description")

## 🔧 Technical Details

### Technologies Used

- **Python 3**: Core programming language
- **JSON**: Data storage format
- **datetime**: Date handling and validation
- **typing**: Type hints for better code quality

### Key Features

- Object-oriented design with `ExpenseTracker` class
- File handling for persistent storage
- Menu-driven interface with input validation
- Error handling for file operations
- Clean code structure with docstrings

## 📊 Sample Data

A sample expense file is included in `data/sample_expenses.json` for testing purposes. To use it:

1. Copy `sample_expenses.json` to `expenses.json`
2. Run the application to see pre-loaded data

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a portfolio project demonstrating Python skills including:

- File handling and data persistence
- Object-oriented programming
- Input validation and error handling
- CLI application development
- Clean code practices

## 🙏 Acknowledgments

Built with Python and passion for clean, maintainable code.

---

**Happy Expense Tracking! 💰**
