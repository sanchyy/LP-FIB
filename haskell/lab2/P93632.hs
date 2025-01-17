eql :: [Int] -> [Int] -> Bool
eql x y
  | length x /= length y    = False
  | otherwise               = and $ zipWith (==) x y

prod :: [Int] -> Int
prod                        = foldl (*) 1

prodOfEvens :: [Int] -> Int
prodOfEvens                 = prod . filter even

powersOf2 :: [Int]
powersOf2                   = iterate (* 2) 1  

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct x y           = sum $ zipWith (*) x y



