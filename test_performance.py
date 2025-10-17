def test_performance():
    sizes = [1000, 5000, 10000, 20000]
    distributions = {
        "Random": lambda n: [random.randint(0, n) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1))
    }
    
    for dist_name, generator in distributions.items():
        print(f"\n=== {dist_name} Data ===")
        for n in sizes:
            data = generator(n)
            
            # Deterministic QuickSort
            start = time.time()
            deterministic_quicksort(data[:])
            det_time = time.time() - start
            
            # Randomized QuickSort
            start = time.time()
            randomized_quicksort(data[:])
            rand_time = time.time() - start
            
            print(f"n={n:6d} | Deterministic: {det_time:.5f}s | Randomized: {rand_time:.5f}s")
