absValue :: Int -> Int
absValue x
  | x >= 0 = x
  | otherwise = -x

power :: Int -> Int -> Int
power x 0 = 1
power x p
  | even p = n*n
  | otherwise = n*n*x
  where
    n = power x (p `div` 2) 

isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime x =  not (hasDivisor (x-1))
  where 
    hasDivisor :: Int -> Bool
    hasDivisor 1 = False 
    hasDivisor n = mod x n == 0 || hasDivisor (n-1)

slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2) 

quickFib :: Int -> Int
quickFib x = snd $ quickFibAux x
    where 
      quickFibAux :: Int -> (Int,Int)
      quickFibAux 0 = (0,0)
      quickFibAux 1 = (0,1)
      quickFibAux n = (s,f+s)
       where
           (f,s) = quickFibAux (n-1)


