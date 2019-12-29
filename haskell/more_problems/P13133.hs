sumMultiples35 :: Integer -> Integer
sumMultiples35 n = sumMultiples n 3 + sumMultiples n 5 - sumMultiples n 15
    where
        sumMultiples :: Integer -> Integer -> Integer
        sumMultiples n x = x * (div (n-1) x) * ((div (n-1) x)+1) `div` 2

fibonacci' :: [Integer]
fibonacci' = (map snd $ iterate (\(a,b) -> (a+b,a)) (1,0)) 

fibonacci :: Int -> Integer
fibonacci n = fibonacci' !! n 

sumEvenFibonaccis :: Integer -> Integer
sumEvenFibonaccis n                     = sum $ filter even $ takeWhile (<n) fibonacci'

largestPrimeFactor :: Int -> Int

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
