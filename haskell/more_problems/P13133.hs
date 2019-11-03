sumMultiples35 :: Integer -> Integer
sumMultiples35 n = sumMultiples n 3 + sumMultiples n 5 - sumMultiples n 15
    where
        sumMultiples :: Integer -> Integer -> Integer
        sumMultiples n x = x * (div (n-1) x) * ((div (n-1) x)+1) `div` 2

fibonacci :: Int -> Integer
fibonacci n = (map snd $ iterate (\(a,b) -> (a+b,a)) (1,0)) !! n

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

isPalindromic :: Integer -> Bool
isPalindromic n                         = n1 == n2 
    where
        n1                              = take m $ show n
        n2                              = take m $ reverse $ show n
        m                               = div (digits n) 2

digits :: Integer -> Int
digits n
  | n < 10                              = 1
  | otherwise                           = 1 + digits (div n 10)
