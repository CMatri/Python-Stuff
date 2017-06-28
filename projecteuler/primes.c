#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include "bitarray.h"
#include <time.h>

void find_primes(int max)
{
  unsigned int *dont_use = malloc(max / 8);

  for(int i = 0; i < max; i++){
    put_bit(dont_use, i, 0);
  }

  for(int i = 3; i < max; i += 2)
  {
    if(get_bit(dont_use, i)) continue;

    for(int j = i + i; j < max; j += i)
    {
      put_bit(dont_use, j, 1);
    }
  }

  for(int i = 3; i < max; i += 2)
  {
    if(!get_bit(dont_use, i))
    {
      printf("%i %s", i, i == max - 1 ? "\n" : "");
    }
  }

  free(dont_use);
}

int main(int argc, char *argv[])
{
  int max = 1000000000;

  clock_t tic = clock();
  find_primes(max);
  clock_t toc = clock();
  printf("Took %f seconds to find primes up to %i.\n", (double)(toc - tic) / CLOCKS_PER_SEC, max);

  return 0;
}
