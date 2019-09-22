absValue :: Int -> Int
absValue x
    | x >= 0 = x
    | otherwise -x

power :: Int - Int -> Int
power 0 = 1
power x p = x * (power x p-1)


isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime x = isPrimeAux x (


slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2) 

quickFib :: Int -> Int
quickFib x = fst $ quickFibAux

quickFibAux :: Int -> (Int,Int)
quickFibAux 0 = (0,0)
quickFibAux 1 = (0,1)
quickFibAux n = (f,s)
    where x = quickFibAux (n-1)
          f = snd x
          s = (fst x) + (snd x)


