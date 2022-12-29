import tkinter as tk
from tkinter import ttk
import random


def center_window(width, height):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    return x, y


# Create the main window
window = tk.Tk()
window.title("Sorting Algorithm Visualizer")

# window.wm_attributes('-fullscreen', True)

# set window width and height
window_width = 800
window_height = 400

# set window position
x, y = center_window(window_width, window_height)
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, int(x), int(y)))

# Create a canvas to draw the bars
canvas = tk.Canvas(window, width=800, height=400)
canvas.pack()

# Create a list of random numbers to sort
numbers = [random.randint(1, 100) for _ in range(80)]

# Create a bar for each number
bars = []
colors = ["blue", "red", "green", "yellow", "orange", "purple", "pink"]
color = random.choice(colors)
for i, number in enumerate(numbers):
    x1 = i * 10
    y1 = 400 - number
    x2 = x1 + 10
    y2 = 400

    bar = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    bars.append(bar)


# Create a function to update the visualizer after each swap
def update_visualizer():
    for i, bar in enumerate(bars):
        x1, y1, x2, y2 = canvas.coords(bar)
        y1 = 400 - numbers[i]
        y2 = 400
        canvas.coords(bar, x1, y1, x2, y2)


# Create a function to shuffle the list
def shuffle():
    # Shuffle the list
    global numbers, bars
    # Clear the canvas
    canvas.delete("all")
    numbers = [random.randint(1, 100) for _ in range(80)]
    bars = []
    for i, number in enumerate(numbers):
        x1 = i * 10
        y1 = 400 - number
        x2 = x1 + 10
        y2 = 400
        bar = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        bars.append(bar)
    update_visualizer()


# Create a function to sort the list using bubble sort
def bubble_sort():
    # Flag to track whether the list is sorted
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                # Swap the numbers
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # Update the visualizer
                update_visualizer()
                # Sleep for a short period to slow down the sorting process
                window.after(100, window.update())
                # Set the flag to False to continue sorting
                sorted = False


# Create a function to sort the list using selection sort
def selection_sort():
    # Find the minimum element in the list
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the minimum element with the first element
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        # Update the visualizer
        update_visualizer()
        # Sleep for a short period to slow down the sorting process
        window.after(100, window.update())


# Create a function to sort the list using quicksort
def quicksort(start, end):
    # Check if the start and end indices are valid
    if start >= end:
        return

    # Choose the pivot element
    pivot = numbers[end]

    # Initialize the left and right indices
    left = start
    right = end - 1

    # Partition the list around the pivot
    while left <= right:
        # Find the first element that is greater than the pivot
        while left <= right and numbers[left] < pivot:
            left += 1
        # Find the last element that is less than the pivot
        while left <= right and numbers[right] >= pivot:
            right -= 1
        # Swap the elements if necessary
        if left <= right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            # Update the visualizer
            update_visualizer()
            # Sleep for a short period to slow down the sorting process
            window.after(100, window.update())
            left += 1
            right -= 1

    # Swap the pivot element with the left element
    numbers[left], numbers[end] = numbers[end], numbers[left]
    # Update the visualizer
    update_visualizer()
    # Sleep for a short period to slow down the sorting process
    window.after(100, window.update())

    # Recursively sort the left and right sublists
    quicksort(start, left - 1)
    quicksort(left + 1, end)


def heap_sort():
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(numbers)
    for i in range(n, -1, -1):
        heapify(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
        update_visualizer()
        window.after(100, window.update())


def merge_sort():
    def merge_sort_helper(arr, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        merge_sort_helper(arr, start, mid)
        merge_sort_helper(arr, mid + 1, end)

        merge(arr, start, mid, end)

    def merge(arr, start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]

        i = j = 0
        k = start
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        update_visualizer()
        window.after(100, window.update())

    merge_sort_helper(numbers, 0, len(numbers) - 1)


def insertion_sort():
    for i in range(1, len(numbers)):
        j = i - 1
        nxt_element = numbers[i]

        while (numbers[j] > nxt_element) and (j >= 0):
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = nxt_element
        update_visualizer()
        window.after(100, window.update())


def shell_sort():
    gap = len(numbers) // 2
    while gap > 0:
        for i in range(gap, len(numbers)):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
        update_visualizer()
        window.after(100, window.update())


def count_sort(exp):
    n = len(numbers)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = numbers[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = numbers[i] // exp
        output[count[index % 10] - 1] = numbers[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(numbers)):
        numbers[i] = output[i]
        update_visualizer()
        window.after(100, window.update())


def radix_sort():
    max1 = max(numbers)
    exp = 1
    while max1 // exp > 0:
        count_sort(exp)
        exp *= 10
        update_visualizer()
        window.after(100, window.update())


# Create a dropdown menu to choose the sort type
sort_type = tk.StringVar()
sort_type.set("Bubble Sort")
sorting_algorithms = ["Bubble Sort",
                      "Selection Sort",
                      "Quicksort",
                      "Heap Sort",
                      "Merge Sort",
                      "Insertion Sort",
                      "Shell Sort",
                      "Radix Sort", ]
sort_menu = ttk.Combobox(window, textvariable=sort_type, values=sorting_algorithms)
sort_menu.pack()


# Create a function to sort the list using the selected sort type
def sort():
    # Get the selected sort type
    sort_type = sort_menu.get()

    # Sort the list using the selected sort type
    if sort_type == "Bubble Sort":
        bubble_sort()
    elif sort_type == "Selection Sort":
        selection_sort()
    elif sort_type == "Quicksort":
        quicksort(0, len(numbers) - 1)
    elif sort_type == "Heap Sort":
        heap_sort()
    elif sort_type == "Merge Sort":
        merge_sort()
    elif sort_type == "Insertion Sort":
        insertion_sort()
    elif sort_type == "Shell Sort":
        shell_sort()
    elif sort_type == "Radix Sort":
        radix_sort()


# Create a button to start the sorting process
sort_button = tk.Button(window, text="Sort", command=sort)
sort_button.pack()

# Create a button to shuffle the list
shuffle_button = tk.Button(window, text="Shuffle", command=shuffle)
shuffle_button.pack()

# Run the main loop
window.mainloop()
