myLength :: [Int] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum [x] = x
myMaximum (x:xs)
  | x > m       = x
  | otherwise   = m
    where m     = myMaximum xs

average :: [Int] -> Float
average x   = suma / len
  where 
      suma  = fromIntegral(sum x) :: Float
      len   = fromIntegral(myLength x) :: Float

buildPalindrome :: [Int] -> [Int]
buildPalindrome []      = []
buildPalindrome x  = reverse x ++ x

remove :: [Int] -> [Int] -> [Int]
remove [] [] = []
remove [] y  = []
remove x  [] = x
remove (x:xs) y
  | elem x y  = remove xs y
  | otherwise = x : (remove xs y)


flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs)  = x ++ (flatten xs)

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens []   = ([],[])
oddsNevens x = (f,s)
    where 
        f = filter odd  x
        s = filter even x

isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime x =  not (hasDivisor (x-1))
  where
    hasDivisor :: Int -> Bool
    hasDivisor 1 = False
    hasDivisor n = mod x n == 0 || hasDivisor (n-1)


primeDivisors :: Int -> [Int] 
primeDivisors x
    | isPrime x = [x]
    | otherwise = primeDivs x 2
    where
        primeDivs :: Int -> Int -> [Int]
        primeDivs x y 
          | y > (div x 2) = []
          | ((mod x y) == 0) && (isPrime y) = y : primeDivs x (y+1)
          | otherwise = primeDivs x (y+1)
