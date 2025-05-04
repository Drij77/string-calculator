class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
            
        # Check for custom delimiter
        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]  # Getting the delimiter after //
            numbers = parts[1]
            
        # Replace newlines with delimiter and split
        numbers = numbers.replace("\n", delimiter)
        number_list = numbers.split(delimiter)
        
        # Convert to integers and check for negatives
        negatives = []
        total = 0
        
        for num in number_list:
            if num:  # Skip empty strings
                value = int(num)
                if value < 0:
                    negatives.append(str(value))
                total += value
                
        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(negatives)}")
            
        return total