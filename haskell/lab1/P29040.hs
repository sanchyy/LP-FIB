insert :: [Int] -> Int -> [Int]
insert [] x     = [x]
insert (x:xs) y
  | x < y       = x : (insert xs y)
  | otherwise   = y : x : xs

isort :: [Int] -> [Int]
isort []        = []
isort (x:xs)    = insert(isort xs) x

remove :: [Int] -> Int -> [Int]
remove [] _     = []
remove (x:xs) y
  | x == y      = xs
  | otherwise   = x : (remove xs y)

ssort :: [Int] -> [Int]
ssort []        = []
ssort x         = min : y
    where
        y       = ssort(remove x min)
        min     = minimum x

merge :: [Int] -> [Int] -> [Int]
merge [] y      = y
merge x []      = x
merge (x:xs) (y:ys)
  | x <= y      = x : (merge xs (y:ys))
  | otherwise   = y : (merge (x:xs) ys)

msort :: [Int] -> [Int]
msort []        = []
msort [x]       = [x]
msort x         = merge (msort x1) (msort x2)
    where 
        x1      = take l x
        x2      = drop l x
        l       = div (length x) 2

qsort :: [Int] -> [Int]
qsort []        = []
qsort (x:xs)    = sSort ++ [x] ++ bSort
    where
        sSort   = qsort [a | a <- xs, a <= x]
        bSort   = qsort [a | a <- xs, a > x ]

genQsort :: Ord a => [a] -> [a]
genQsort []     = []
genQsort (x:xs) = sSort ++ [x] ++ bSort
    where 
        sSort   = genQsort [n | n <- xs, n <= x]
        bSort   = genQsort [n | n <- xs, n > x ]
