def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(up_to):
    prime_list = []
    is_prime_array = [True] * (up_to + 1)
    for num in range(2, up_to + 1):
        if is_prime_array[num]:
            prime_list.append(num)
            for multiple in range(num * num, up_to + 1, num):
                is_prime_array[multiple] = False
    return prime_list


def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    maria_wins = 0
    ben_wins = 0
    for round_num in nums:
        primes = generate_primes(round_num)
        current_player = 0  # 0 for Maria, 1 for Ben
        while primes:
            current_prime = primes.pop(0)
            primes = [p for p in primes if p % current_prime != 0]
            current_player = 1 - current_player  # Switch turns
        if current_player == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
