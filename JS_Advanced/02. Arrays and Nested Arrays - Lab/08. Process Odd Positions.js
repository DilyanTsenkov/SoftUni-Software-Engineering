function odd(numbers) {
    return numbers.filter((a, i) => i % 2 !== 0)
      .map(x => x * 2)
      .reverse()
      .join(' ');
  }
  
odd([10, 15, 20, 25]);
odd([3, 0, 10, 4, 7, 3]);