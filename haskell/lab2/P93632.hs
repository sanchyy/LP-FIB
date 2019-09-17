import Data.List

eql :: [Int] -> [Int] -> Bool
eql x y = 

prod :: [Int] -> Int
prod = foldl (*) 1

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct x y = sum $ zipWith (*) x y



