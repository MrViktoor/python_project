def compute_tax(status: str, tax_income: float):
    if tax_income < 1:
        return f"task income cannot be negative"
    if tax_income < 50000:
        return "Your task income cannot be "
