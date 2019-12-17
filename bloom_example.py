from random import SystemRandom

from pybloom import ScalableBloomFilter


def main():
  bloom = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
  random = SystemRandom()

  print('Sample hashes:')
  for i in range(0, 10000):
    random_hash = hex(random.getrandbits(256))
    bloom.add(random_hash)

    if i % 1000 == 0:
      print(random_hash)

  print(f'~{len(bloom)} hashes added to bloom filter.')

  print()
  try:
    while True:
      user_hash = input('Enter hash to check: ')
      if not user_hash:
        break

      print(user_hash in bloom)
  except (EOFError, KeyboardInterrupt):
    pass


if __name__ == '__main__':
  main()
