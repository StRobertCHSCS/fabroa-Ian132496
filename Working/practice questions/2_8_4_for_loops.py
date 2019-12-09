# get numbers from user
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

if start < end:
    for i in range(start, end + 1):
        print(i)

elif start >= end:
    for i in range(start, end - 1, -1):
        print(i)
