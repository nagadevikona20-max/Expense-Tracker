#!/usr/bin/env python3
"""
Expense Tracker - A CLI application for managing daily expenses
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class ExpenseTracker:
    """Main class for managing expenses"""

    def __init__(self, data_file: str = "data/expenses.json"):
        self.data_file = data_file
        self.expenses: List[Dict] = []
        self._ensure_data_directory()
        self.load_expenses()

    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.expenses = json.load(f)
                print(f"✓ Loaded {len(self.expenses)} expenses from file")
            except json.JSONDecodeError:
                print("⚠ Error reading data file. Starting fresh.")
                self.expenses = []
        else:
            print("ℹ No existing data found. Starting fresh.")
            self.expenses = []

    def save_expenses(self):
        """Save expenses to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.expenses, f, indent=2)
            print("✓ Expenses saved successfully")
        except Exception as e:
            print(f"✗ Error saving expenses: {e}")

    def add_expense(self, date: str, category: str, amount: float, description: str):
        """Add a new expense"""
        expense = {
            "id": len(self.expenses) + 1,
            "date": date,
            "category": category.lower(),
            "amount": amount,
            "description": description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✓ Expense added successfully (ID: {expense['id']})")

    def view_all_expenses(self):
        """Display all expenses"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return

        print("\n" + "="*80)
        print(
            f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<30}")
        print("="*80)

        for expense in self.expenses:
            print(f"{expense['id']:<5} {expense['date']:<12} {expense['category']:<15} "
                  f"${expense['amount']:<9.2f} {expense['description']:<30}")
        print("="*80)

    def calculate_total(self) -> float:
        """Calculate total expenses"""
        return sum(expense['amount'] for expense in self.expenses)

    def monthly_summary(self, month: Optional[str] = None):
        """Show monthly expense summary"""
        if not self.expenses:
            print("\nNo expenses to summarize.")
            return

        if month:
            filtered = [
                e for e in self.expenses if e['date'].startswith(month)]
            if not filtered:
                print(f"\nNo expenses found for {month}")
                return
            total = sum(e['amount'] for e in filtered)
            print(f"\n{'='*50}")
            print(f"Monthly Summary for {month}")
            print(f"{'='*50}")
            print(f"Total Expenses: ${total:.2f}")
            print(f"Number of Transactions: {len(filtered)}")
        else:
            # Group by month
            monthly_data = {}
            for expense in self.expenses:
                month_key = expense['date'][:7]  # YYYY-MM
                if month_key not in monthly_data:
                    monthly_data[month_key] = []
                monthly_data[month_key].append(expense)

            print(f"\n{'='*50}")
            print("All Months Summary")
            print(f"{'='*50}")
            for month_key in sorted(monthly_data.keys()):
                total = sum(e['amount'] for e in monthly_data[month_key])
                count = len(monthly_data[month_key])
                print(f"{month_key}: ${total:.2f} ({count} transactions)")

    def filter_by_category(self, category: str):
        """Filter and display expenses by category"""
        category = category.lower()
        filtered = [e for e in self.expenses if e['category'] == category]

        if not filtered:
            print(f"\nNo expenses found for category: {category}")
            return

        print(f"\n{'='*80}")
        print(f"Expenses in category: {category.upper()}")
        print(f"{'='*80}")
        print(f"{'ID':<5} {'Date':<12} {'Amount':<10} {'Description':<30}")
        print("="*80)

        total = 0
        for expense in filtered:
            print(f"{expense['id']:<5} {expense['date']:<12} "
                  f"${expense['amount']:<9.2f} {expense['description']:<30}")
            total += expense['amount']

        print("="*80)
        print(f"Total for {category}: ${total:.2f}")

    def category_summary(self):
        """Show expense summary by category"""
        if not self.expenses:
            print("\nNo expenses to summarize.")
            return

        category_totals = {}
        for expense in self.expenses:
            cat = expense['category']
            category_totals[cat] = category_totals.get(
                cat, 0) + expense['amount']

        print(f"\n{'='*50}")
        print("Category-wise Summary")
        print(f"{'='*50}")
        print(f"{'Category':<20} {'Total':<15} {'Percentage'}")
        print("="*50)

        total = sum(category_totals.values())
        for category in sorted(category_totals.keys()):
            amount = category_totals[category]
            percentage = (amount / total) * 100
            print(f"{category.capitalize():<20} ${amount:<14.2f} {percentage:.1f}%")
        print("="*50)
        print(f"{'Grand Total':<20} ${total:.2f}")

    def export_summary(self, filename: str = "data/expense_summary.txt"):
        """Export expense summary to a text file"""
        try:
            with open(filename, 'w') as f:
                f.write("EXPENSE TRACKER SUMMARY REPORT\n")
                f.write("="*80 + "\n\n")
                f.write(
                    f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                # Total expenses
                total = self.calculate_total()
                f.write(f"Total Expenses: ${total:.2f}\n")
                f.write(f"Total Transactions: {len(self.expenses)}\n\n")

                # Category summary
                category_totals = {}
                for expense in self.expenses:
                    cat = expense['category']
                    category_totals[cat] = category_totals.get(
                        cat, 0) + expense['amount']

                f.write("CATEGORY BREAKDOWN\n")
                f.write("-"*80 + "\n")
                for category in sorted(category_totals.keys()):
                    amount = category_totals[category]
                    percentage = (amount / total) * 100
                    f.write(
                        f"{category.capitalize():<20} ${amount:<14.2f} {percentage:.1f}%\n")

                f.write("\n" + "="*80 + "\n")
                f.write("ALL EXPENSES\n")
                f.write("="*80 + "\n")
                f.write(
                    f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}\n")
                f.write("-"*80 + "\n")

                for expense in self.expenses:
                    f.write(f"{expense['date']:<12} {expense['category']:<15} "
                            f"${expense['amount']:<9.2f} {expense['description']}\n")

            print(f"✓ Summary exported to {filename}")
        except Exception as e:
            print(f"✗ Error exporting summary: {e}")


def validate_date(date_str: str) -> bool:
    """Validate date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_amount(amount_str: str) -> Optional[float]:
    """Validate and convert amount to float"""
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("✗ Amount must be positive")
            return None
        return amount
    except ValueError:
        print("✗ Invalid amount. Please enter a numeric value")
        return None


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("EXPENSE TRACKER")
    print("="*50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Monthly Summary")
    print("5. Filter by Category")
    print("6. Category-wise Summary")
    print("7. Export Summary Report")
    print("8. Exit")
    print("="*50)


def main():
    """Main function to run the expense tracker"""
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == '1':
            # Add expense
            print("\n--- Add New Expense ---")
            date = input(
                "Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date:
                date = datetime.now().strftime('%Y-%m-%d')
            elif not validate_date(date):
                print("✗ Invalid date format. Use YYYY-MM-DD")
                continue

            category = input(
                "Enter category (e.g., food, transport, utilities): ").strip()
            if not category:
                print("✗ Category cannot be empty")
                continue

            amount_str = input("Enter amount: $").strip()
            amount = validate_amount(amount_str)
            if amount is None:
                continue

            description = input("Enter description: ").strip()
            if not description:
                description = "No description"

            tracker.add_expense(date, category, amount, description)

        elif choice == '2':
            # View all expenses
            tracker.view_all_expenses()

        elif choice == '3':
            # Calculate total
            total = tracker.calculate_total()
            print(f"\n{'='*50}")
            print(f"Total Expenses: ${total:.2f}")
            print(f"{'='*50}")

        elif choice == '4':
            # Monthly summary
            month = input(
                "\nEnter month (YYYY-MM) or press Enter for all months: ").strip()
            tracker.monthly_summary(month if month else None)

        elif choice == '5':
            # Filter by category
            category = input("\nEnter category to filter: ").strip()
            if category:
                tracker.filter_by_category(category)
            else:
                print("✗ Category cannot be empty")

        elif choice == '6':
            # Category summary
            tracker.category_summary()

        elif choice == '7':
            # Export summary
            tracker.export_summary()

        elif choice == '8':
            # Exit
            print("\nThank you for using Expense Tracker! Goodbye! 👋")
            break

        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 8")


if __name__ == "__main__":
    main()
