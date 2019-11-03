sumMultiples35 :: Integer -> Integer
sumMultiples35 n                = sum [x | x <- [1..(n-1)], (mod x 3 == 0 || mod x 5 == 0)]

fibonacci :: Int -> Integer
fibonacci 1                             = 1
fibonacci 2                             = 1
fibonacci n                             = fibonacci' 3 (1,1) 
    where
        fibonacci' :: Int -> (Integer, Integer) -> Integer
        fibonacci' i (s1,s2)
          | i == n                      = s1+s2
          | otherwise                   = fibonacci' (i+1) (s1+s2, s1)

sumEvenFibonaccis :: Integer -> Integer
sumEvenFibonaccis n                     = sum $ filter (even) (fibonacci' (1,1) []) 
    where
        fibonacci' :: (Integer, Integer) -> [Integer] -> [Integer]
        fibonacci' (s1,s2) res
          | (s1+s2) >= n                = res ++ [s1+s2] 
          | otherwise                   = fibonacci' (s1+s2,s1) (res++[s1+s2])

largestPrimeFactor :: Int -> Int
largestPrimeFactor n                    = largestPrimeFactor' (n-1)
    where
        largestPrimeFactor' :: Int -> Int
        largestPrimeFactor' x
          | is_prime x && mod n x == 0  = x 
          | otherwise                   = largestPrimeFactor' (x-1) 

is_prime :: Int -> Bool
is_prime 1                              = False
is_prime 2                              = True
is_prime n 
  | (length [x | x <- [2 .. n-1], mod n x == 0]) > 0 = False
  | otherwise = True
