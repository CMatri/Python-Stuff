int dw_index(int x)
{
  return x >> 5;
}

int bit_index(int x)
{
  return x & 0x1f;
}

int get_reserve_size(int max)
{
  return ((max + 0x1f) >> 5) + 1;
}

int get_bit(unsigned int* array, int index)
{
  return (array[dw_index(index)] >> bit_index(index)) & 1;
}

void put_bit(unsigned int* array, int index, int val)
{
  if(val == 1)
    array[dw_index(index)] |= 1 << bit_index(index);
  else if(val == 2)
    array[dw_index(index)] &= ~(1 << bit_index(index));
}
