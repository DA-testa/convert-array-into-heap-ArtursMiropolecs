def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, data, swaps)

def main():
    
    try:
        input_type = input("Enter input type: I for keyboard, F for file: ")
        if input_type.startswith('I'):
            n = int(input(""))
            data = list(map(int, input().split()))
        elif input_type.startswith('F'):
            file_name = "tests/" + input("Enter file name: ")
            with open(file_name, 'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        
        assert len(data) == n
    
        swaps = build_heap(data)
        
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    except Exception as e:
        print(f"Error:{e}")
        return

if __name__ == "__main__":
    main()