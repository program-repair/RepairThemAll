from core.database.engine import count_collected_samples_by_conditions


if __name__ == "__main__":
    counter = count_collected_samples_by_conditions('Cli', 15, 0.8)
    print('counter:', counter)
