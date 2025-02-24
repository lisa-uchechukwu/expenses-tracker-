import uuid
from datetime import datetime

class Expense:
    def __init__(self, title: str, amount: float):
        """Initialize an Expense with a unique ID, title, amount, and timestamps."""
        self.id = str(uuid.uuid4())  # Generates a unique ID
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()  # Stores the creation time (UTC)
        self.updated_at = self.created_at  # Initially same as created_at

    def update(self, title: str = None, amount: float = None):
        """Update title and/or amount, and refresh the updated_at timestamp."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()  # Update timestamp

    def to_dict(self):
        """Return a dictionary representation of the expense."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class ExpenseDatabase:
    def __init__(self):
        """Initialize an empty expense list."""
        self.expenses = []

    def add_expense(self, expense: Expense):
        """Add an expense to the list."""
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """Remove an expense by ID."""
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """Retrieve an expense by its unique ID."""
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if not found

    def get_expense_by_title(self, title: str):
        """Retrieve all expenses with a specific title."""
        return [exp for exp in self.expenses if exp.title.lower() == title.lower()]

    def to_dict(self):
        """Return a list of dictionary representations of all expenses."""
        return [expense.to_dict() for expense in self.expenses]

# ========== TESTING THE CLASSES ==========
if __name__ == "__main__":
    # Create expenses
    expense1 = Expense("breakfast", 3200.00)
    expense2 = Expense("launch", 7600.00)
    expense3 = Expense("dinner", 4500.00)

    # Create the database
    db = ExpenseDatabase()

    # Add expenses to the database
    db.add_expense(expense1)
    db.add_expense(expense2)
    db.add_expense(expense3)

    # Print all expenses in dictionary format
    print("All Expenses:", db.to_dict())

  # Get an expense by ID
    found_expense = db.get_expense_by_id(expense1.id)
    print("\n🔹 Get Expense by ID:")
    print(found_expense.to_dict() if found_expense else "Expense not found")

    # Get expenses by title
    lunch_expenses = db.get_expense_by_title("Lunch")
    print("\n🔹 Get Expenses by Title ('Lunch'):")
    print([exp.to_dict() for exp in lunch_expenses])

    # Update an expense
    expense2.update(amount=10000)
    print("Updated Expense 2:", expense2.to_dict())

    # Remove an expense
    db.remove_expense(expense2.id)
    print("Expenses after removing expense2:", db.to_dict())