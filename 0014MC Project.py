import tkinter as tk
from tkinter import messagebox, ttk

# Dictionary containing locations and distances in km
locations = {
    'Kalutara': 0.00,
    'Panadura': 5.00,
    'Moratuwa': 10.00,
    'Ratmalana': 15.00,
    'Dehiwala': 20.00,
    'Colombo': 25.00,
}

# Function to calculate the ticket price based on the distance between start and end locations
def calculate_price(start_location, end_location):
    return abs(locations[end_location] - locations[start_location])

# Function to handle ticket booking
def book_ticket():
    # Get the selected start and end locations
    start_location = start_location_var.get()
    end_location = end_location_var.get()
    
    # Check if start and end locations are the same
    if start_location == end_location:
        messagebox.showerror("Error", "Start and end locations cannot be the same.")
        return
    
    # Calculate and display the ticket price
    price = calculate_price(start_location, end_location)
    price_var.set(f"Rs.{price:.2f}")

# Function to process the payment
def process_payment():
    try:
        # Retrieve the payment amount entered by the user
        payment = float(payment_entry.get())
        price = float(price_var.get().replace("Rs.", ""))
        
        # Check if payment is sufficient
        if payment >= price:
            # Calculate and display change if payment is sufficient
            change = payment - price
            change_var.set(f"Rs.{change:.2f}")
            messagebox.showinfo("Success", f"Ticket booked successfully! Change to be returned: Rs.{change:.2f}")
            show_review_section()  # Display the review section
        else:
            # Show error if payment is insufficient
            messagebox.showerror("Error", "Insufficient payment. Please enter the correct amount.")
    
    except ValueError:
        # Handle non-numeric input errors
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

# Function to show the review section for user feedback
def show_review_section():
    review_label.grid(row=9, column=0, sticky="e")  # Show review prompt label
    review_var.set(None)  # Reset review selection
    # Display star rating options
    for i, button in enumerate(star_buttons):
        button.grid(row=10 + i, column=1, sticky="w")
    submit_review_button.grid(row=15, column=0, columnspan=2, pady=10)

# Function to submit the user's review
def submit_review():
    rating = review_var.get()
    if rating:
        messagebox.showinfo("Thank You!", f"Thank you for your feedback! You rated us {rating} star(s).")
        messagebox.showinfo("Goodbye", "Thank you for traveling with us!")
        reset_form()  # Reset form after submitting the review
    else:
        messagebox.showerror("Error", "Please select a rating before submitting.")

# Function to reset the booking form and review section
def reset_form():
    start_location_var.set("Kalutara")
    end_location_var.set("Colombo")
    price_var.set("")
    payment_entry.delete(0, tk.END)
    change_var.set("")
    review_var.set(None)
    for button in star_buttons:
        button.grid_remove()  # Hide star buttons after reset

# Create the main application window
root = tk.Tk()
root.title("ABC Express")
root.geometry("400x600")
root.configure(bg="#f0f0f0")  # Set light background color

# Title label
tk.Label(root, text="ABC Express", font=("Helvetica", 20, 'bold'), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)

# Start location label and dropdown menu
tk.Label(root, text="Start Location:", bg="#f0f0f0").grid(row=2, column=0, sticky="e")
start_location_var = tk.StringVar(value="Kalutara")
start_location_menu = ttk.Combobox(root, textvariable=start_location_var, values=list(locations.keys()), state='readonly')
start_location_menu.grid(row=2, column=1)

# End location label and dropdown menu
tk.Label(root, text="End Location:", bg="#f0f0f0").grid(row=3, column=0, sticky="e")
end_location_var = tk.StringVar(value="Colombo")
end_location_menu = ttk.Combobox(root, textvariable=end_location_var, values=list(locations.keys()), state='readonly')
end_location_menu.grid(row=3, column=1)

# Button to calculate price
tk.Button(root, text="Calculate Price", command=book_ticket, bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=3, pady=10)

# Price label and display
tk.Label(root, text="Price:", bg="#f0f0f0").grid(row=5, column=0, sticky="e")
price_var = tk.StringVar()
tk.Label(root, textvariable=price_var, bg="#f0f0f0").grid(row=5, column=1)

# Payment entry label and input field
tk.Label(root, text="Payment:", bg="#f0f0f0").grid(row=6, column=0, sticky="e")
payment_entry = tk.Entry(root)
payment_entry.grid(row=6, column=1)

# Button to process payment
tk.Button(root, text="Process Payment", command=process_payment, bg="#2196F3", fg="white").grid(row=7, column=0, columnspan=3, pady=10)

# Change label and display
tk.Label(root, text="Change:", bg="#f0f0f0").grid(row=8, column=0, sticky="e")
change_var = tk.StringVar()
tk.Label(root, textvariable=change_var, bg="#f0f0f0").grid(row=8, column=1)

# Review section setup
review_label = tk.Label(root, text="Rate your experience:", bg="#f0f0f0")
review_var = tk.IntVar()
star_buttons = [tk.Radiobutton(root, text=f"{i+1} Star{'s' if i > 0 else ''}", variable=review_var, value=i+1, bg="#f0f0f0") for i in range(5)]
submit_review_button = tk.Button(root, text="Submit Review", command=submit_review, bg="#FF9800", fg="white")

# Reset button to clear form
reset_button = tk.Button(root, text="Reset", command=reset_form, bg="#F44336", fg="white")
reset_button.grid(row=16, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
