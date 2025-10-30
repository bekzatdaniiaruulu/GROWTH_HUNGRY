def advanced_tip_calculator():
    
    try:
        bill_amount = float(input("Enter the bill amount (before tip): $"))
        tip_percentage = float(input("Enter the tip percentage: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return


    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount

    
    if tip_percentage > 20:
        print("\n*** Thank you for your generosity! 🌟 ***")

    print(f"\nTip amount: ${tip_amount:.2f}")
    print(f"Total bill (including tip): ${total_bill:.2f}")

    
    try:
        number_of_people = int(input("\nHow many people are splitting the bill? "))
    except ValueError:
        print("Error: The number of people must be a whole number.")
        return

    
    if number_of_people < 2:
        print("A minimum of 2 people is required to split the bill.")
        return

 
    people_names = []
    print("\nPlease enter the name for each person:")
    for i in range(number_of_people):
        name = input(f"Person {i + 1}'s name: ")
        people_names.append(name)
        
  
    sum_for_each_person = total_bill / number_of_people

    print("\n" + "=" * 35)
    print("✅ FINAL BREAKDOWN:")
    
  
    for name in people_names:
        print(f"💰 {name} needs to pay: ${sum_for_each_person:.2f}")
    print("=" * 35)

advanced_tip_calculator()