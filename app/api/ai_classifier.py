def classify_intent(user_query):
    # Basic intent classification based on keywords
    user_query= user_query.lower()
    if "create" in user_query and "vm" in user_query:
        return "create_vm"
    elif "resize" in user_query and "vm" in user_query:
        return "resize_vm"
    elif "delete" in user_query and "vm" in user_query:
        return "delete_vm"
    elif "create" in user_query and "network" in user_query:
        return "create_network"
    elif "delete" in user_query and "volume" in user_query:
        return "delete_volume"
    elif "usage" in user_query:
        return "usage_query"
    else:
        return "unknown_intent"

def extract_parameters(user_query):
    params = {}
    
    # Simple string matching for 'name' and 'flavor'
    if "named" in user_query:
        # Extracts the name after 'named'
        params['name'] = user_query.split("named")[-1].split()[0]
    
    if "flavor" in user_query:
        try:
            # Try extracting flavor after the word 'flavor'
            flavor_part = user_query.split("flavor")[-1].split()
            if len(flavor_part) > 1:  # Check if there's a word after 'flavor'
                params['flavor'] = flavor_part[1]
            else:
                params['flavor'] = None  # If no flavor is specified, assign None
        except IndexError:
            params['flavor'] = None  # Handle edge case
    return params

if __name__ == "__main__":
    # Example query
    user_query = "Create a VM named dev-box with flavor S.4"

    # Classify intent
    intent = classify_intent(user_query)
    print(f"Intent: {intent}")

    # Extract parameters
    params = extract_parameters(user_query)
    print(f"Parameters: {params}")
