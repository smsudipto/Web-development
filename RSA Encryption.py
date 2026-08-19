def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


p = int(input("p="))
q = int(input("q="))
e = int(input("e="))
m = int(input("m="))


if not is_prime(p) or not is_prime(q):
    print("Invalid Input.")
    exit()


if p == q:
    print("Invalid Input.")
    exit()


n = p * q
phi = (p - 1) * (q - 1)


if not (1 < e < phi) or gcd(e, phi) != 1:
    print("Invalid Input.")
    exit()


if not (0 <= m < n):
    print("Invalid Input.")
    exit()


d = find_d(e, phi)


c = pow(m, e, n)


print("RSA OUTPUT.")
print("n =", n)
print("phi =", phi)
print("d =", d)
print("c =", c)