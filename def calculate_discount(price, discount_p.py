def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after discount if discount_percent is 20% or higher; otherwise, the original price.
    """
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

def main():
    
    try:
        original_price = float(input("500"))
        discount_percent = float(input("15"))
        
        
        final_price = calculate_discount(original_price, discount_percent)
        
        
        print(f"The final price after applying the discount is: ${final_price:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()