from interaction_checkers import check_interaction

def main():
    print("Welcome to Drug Interaction Checker!")
    drug1 = input("Enter the first drug name: ").strip().lower()
    drug2 = input("Enter the second drug name: ").strip().lower()
    
    interaction_result = check_interaction(drug1, drug2)
    
    if interaction_result:
        print(f"Warning: Interaction found - {interaction_result}")
    else:
        print("No interaction found between these drugs.")

if __name__ == "__main__":
    main()
