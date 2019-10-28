ones :: [Integer]
ones                            = repeat 1 

nats :: [Integer]
nats                            = iterate (+1) 0

ints :: [Integer]
ints                            = iterate integers 0
    where
        integers :: Integer -> Integer
        integers x
          | x > 0               = -x
          | otherwise           = 1 - x

triangulars :: [Integer]
triangulars                     = scanl (+) 0 $ iterate (+1) 1

factorials :: [Integer]
factorials                      = scanl (*) 1 $ iterate (+1) 1

fibs :: [Integer]
fibs                            = fibo 0 1
    where 
        fibo :: Integer -> Integer -> [Integer]
        fibo x y                = x : (fibo y (x+y))

primes :: [Integer]
primes                          = filter isPrime $ iterate (+1) 1
    where
        isPrime :: Integer -> Bool
        isPrime 1               = False
        isPrime 2               = True
        isPrime n
          | even n              = False
          | otherwise           = isPrimeAux 3
             where
              isPrimeAux :: Integer -> Bool
              isPrimeAux x
                | x >= div n 2  = True
                | mod n x == 0  = False 
                | otherwise     = isPrimeAux (x+2)

hammings :: [Integer]
hammings = 1 : (merge (map (*2) hammings) $ merge ( map (*3) hammings) (map (*5) hammings))
    where
        merge :: [Integer] -> [Integer] -> [Integer]
        merge (x:xs) (y:ys)
          | x < y               = x : merge xs (y:ys)
          | x == y              = x : merge xs ys
          | otherwise           = y : merge (x:xs) ys

lookNsay :: [Integer]
lookNsay                        = iterate look 1
    where 
        look :: Integer -> Integer
        look n                  = read $ say $ show n
            where 
                say :: [Char] -> [Char]
                say []          = []
                say cs          = (show x) ++ [pr] ++ say q
                    where
                        pr      = head cs
                        x       = length $ takeWhile (==pr) cs
                        q       = dropWhile (==pr) cs

tartaglia :: [[Integer]]
tartaglia                       = iterate nextIteration [1]
    where 
        nextIteration :: [Integer] -> [Integer]
        nextIteration n = zipWith (+) (0:n) (n++[0])
