absValue :: Int -> Int
absValue x
    | x >= 0 = x
    | otherwise -x

power :: Int - Int -> Int
power 0 = 1
power x p = x * (power x p-1)


isPrime :: Int -> Bool


slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2) 

quickFib :: Int -> Int

