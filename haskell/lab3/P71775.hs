countIf :: (Int -> Bool) -> [Int] -> Int 
countIf b x             = length $ filter b x 

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam x fs                = [map f x | f <- fs]

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 n fs               = map (\x -> [f x | f <- fs]) n

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl b f n x     = foldl f n $ filter b x

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert b [] n           = [n]
insert b (x:xs) n
  | b x n               = x : insert b xs n
  | otherwise           =  n : x : xs


insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort b xs      = foldl (insert b) [] xs
