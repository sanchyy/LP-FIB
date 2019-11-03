-- I V X  L  C   D   M
-- 1 5 10 50 100 500 1000
roman2int :: String -> Int
roman2int str           = solver 0 $ map parse str 
    where
        parse :: Char -> Int
        parse 'I'       = 1
        parse 'V'       = 5
        parse 'X'       = 10
        parse 'L'       = 50
        parse 'C'       = 100
        parse 'D'       = 500
        parse 'M'       = 1000
        
        solver :: Int -> [Int] -> Int
        solver x []     = x
        solver x [y]    = x + y
        solver x (x1:x2:xs)
          | x1 < x2     = solver (x+(x2-x1)) xs
          | otherwise   = solver (x+x1) (x2:xs)

