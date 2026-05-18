
# CATEGORIES ( Sets )

# Property:  Sets don't contain duplicates 
categories = ['electronics', 'computers', 'mobiles', 'audio', 'video', 'cameras', "cameras"]

categories_set = set(categories)

print("Categories Sets: ", categories_set)

# add electronices and computer again

categories_set.add('electronics')

categories_set.add('computers')

print("Updated Categories: ", categories_set)

# Check Categories using in method

is_electronics_present = 'electronics' in categories_set
print("is_electronics_present: ", is_electronics_present)

print('Unique elements: ', len(categories_set))