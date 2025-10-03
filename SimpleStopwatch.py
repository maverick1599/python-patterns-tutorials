import time

# Simple Stopwatch

input("Press Enter to start the stopwatch...")
start_time = time.time()

input("Press Enter to stop the stopwatch...")
end_time = time.time()

elapsed = end_time - start_time
print(f"Elapsed time: {round(elapsed, 2)} seconds")
