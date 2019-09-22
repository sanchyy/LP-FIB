myLength :: [Int] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum [x] = x
myMaximum (x:xs)
    | x > m = x
    | otherwise = m
    where m = myMaximum xs

average :: [Int] -> Float
average x = sum x `div` genericLength x

buildPalindrome :: [Int] -> [Int]


remove :: [Int] -> [Int] -> [Int]
remove [] [] = []
remove [] y  = []
remove x  [] = x
