fizzBuzz :: [Either Int String]
fizzBuzz = [wich_value g h x | x <- [1..], let g = mod x 3 == 0, let h = mod x 5 == 0]
    where 
        which_value g h x
          | g && h = Right "FizzBuzz"
          | g = Right "Fizz"
          | h = Right "Buzz"
          | otherwise Left x
