def groundhog_day(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        previous_string = strings[i - 1]
        differing_indices = [index for index in range(len(current_string))
                             if current_string[index] != previous_string[index]]
        if len(differing_indices) > 2:
            return i, *differing_indices
    return 0, 0
