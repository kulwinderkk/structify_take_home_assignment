def get_chord_pair(radian_measures, identifiers):
    '''
    
    Since it is given that radians will be sorted in ascending order, I believe that there
    will be few cases where identifiers are not ordered. It could also be like ['s1', 's3', 'e3', 'e2', 's2', 'e1']
    To tackle it I created this function.
    
    INPUT 1: List of radian measurement
    INPUT 2: List of identifiers as string writtern in follwoing format
             Example -> ['s1', 's2', 'e1', 'e2']
    
    OUTPUT: List of chord pairs with starting and ending radian measurements are enclosed in tuple
            Example -> [(1.22, 1.33), (0.67, 1.88)]
    
    '''
    
    assert isinstance(radian_measures, list), "Error: radian_measures should be a list"
    assert isinstance(identifiers, list), "Error: identifiers should be a list"
    for item in identifiers:
        assert isinstance(item, str), "Error: identifier item should be a string"
    
    
    start_end_val=[]
    #total number of chords that can be made
    num_chords= int(len(radian_measures)/2)
    #place holder to save chord pair start and end radians as tuple
    chord=[]
    chord_ac=[]
    for identifier in identifiers:
        ids=list(identifier)
        start_end_val.append((ids[0], ids[1]))
   
    for each_chord in range(1, num_chords+1):
        for index, each_identifier in enumerate(start_end_val):
            if each_identifier[0]=='s' and int(each_identifier[1])==each_chord:
                temp1=radian_measures[index]

            elif each_identifier[0]=='e' and int(each_identifier[1])==each_chord:
                temp2=radian_measures[index]

        chord.append((temp1, temp2))
        if temp1<temp2:
            chord_ac.append((temp1, temp2))
        else: 
            chord_ac.append((temp2, temp1))
    # Rearrange the list based on the starting element of each tuple
    sorted_chords = sorted(chord_ac, key=lambda x: x[0])
    
    return sorted_chords

def check_intersection(chord1, chord2):
    '''
    INPUT: Chord1 - tuple(start , end radians)
           Chord2 - tuple(start , end radians)
    OUTPUT : True or False
             True - If chords intersect
             False - If chords do not intersect
    
    '''
    start1, end1 = chord1
    start2, end2 = chord2

    # Calculate angular ranges
    range1 = [start1, end1]
    range2 = [start2, end2]

    if range1[0] <= range2[1] and range1[1] >= range2[0]:
        return True  # Chords intersect
    else:
        return False  # Chords do not intersect

    
def count_intersections(chords):
    '''
    INPUT : List of Chords. Each chord is a pair of start and end radian values
    OUTPUT : Count of Intersection
    
    '''
    
    intersection_count = 0

    # Iterate over all pairs of chords
    for i in range(len(chords)):
        for j in range(i + 1, len(chords)):
            chord1 = chords[i]
            chord2 = chords[j]

            # Check if chords intersect
            if check_intersection(chord1, chord2):
                intersection_count += 1

    return intersection_count


if __name__=="__main__":
    import ast

    def is_ascending(lst):
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

    # Function to get valid input for a list
    def get_valid_input_radian(prompt):
        while True:
            user_input = input(prompt)
            try:
                result = ast.literal_eval(user_input)
                if isinstance(result, list) and len(result)%2==0 and is_ascending(result):
                    return result
            except (SyntaxError, ValueError):
                print("Invalid input. Please enter a valid list.")
    
    def get_valid_input_identifier(prompt):
        while True:
            user_input = input(prompt)
            try:
                result = ast.literal_eval(user_input)
                if isinstance(result, list) and all(isinstance(item, str) for item in result) and len(result)%2==0:
                    return result
            except (SyntaxError, ValueError):
                print("Invalid input. Please enter a valid list.")

    # Get valid radian_measures input
    radian_measures = get_valid_input_radian("Enter the list of radian measurements for start and end of chords:")

    # Get valid identifiers input
    identifiers = get_valid_input_identifier("Enter the list of identifiers specifying start and end of chords as ['s1', 'e1',...]\n where 's1' represents start of chord 1 and 'e1' represents end of chord 2:")

    # Now you have valid radian_measures and identifiers
    print("Valid Radian Measures:", radian_measures)
    print("Valid Identifiers:", identifiers)
    
    chords=get_chord_pair(radian_measures, identifiers)
    count=count_intersections(chords)
    print(f"Total Number of Chord Intersections: {count}")