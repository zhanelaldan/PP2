def count_upper_lower(s):

    upper_count = 0
    lower_count = 0

    for c in s:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1    
    print("no of upper:", upper_count) 
    print("no of lower:", lower_count)       

count_upper_lower("KazakhBritishTechnicalUniversity")
