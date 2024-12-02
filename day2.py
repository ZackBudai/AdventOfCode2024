with open("day2.txt", "r") as txt_file:
  data = txt_file.read()

def is_valid_sequence(numbers):
    if len(numbers) < 2:
        return True
    first_diff = numbers[1] - numbers[0]
    if first_diff == 0: 
        return False
    
    expected_direction = first_diff > 0  
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if expected_direction and (diff <= 0 or diff > 3):
            return False
        if not expected_direction and (diff >= 0 or diff < -3):
            return False
    
    return True

def is_safe_with_dampener(numbers):

    if is_valid_sequence(numbers):
        return True
 
    for i in range(len(numbers)):
        dampened_sequence = numbers[:i] + numbers[i+1:]
        if is_valid_sequence(dampened_sequence):
            return True
    
    return False

def count_safe_reports_with_dampener(input_data):
    safe_count = 0
    
    for line in input_data.strip().split('\n'):

        numbers = list(map(int, line.split()))
        if is_safe_with_dampener(numbers):
            safe_count += 1
    
    return safe_count

result = count_safe_reports_with_dampener(data)
print(f"Number of safe reports with Problem Dampener: {result}")  

