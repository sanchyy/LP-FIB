myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f n []          = n
myFoldl f n (x:xs)      = myFoldl f (f n x) xs

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f n []          = n
myFoldr f n (x:xs)      = f x (myFoldr n xs)

myIterate :: (a -> a) -> a -> [a]
myIterate f n           = n : myIterate f (f n) 

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil f g x

myMap :: (a -> b) -> [a] -> [b]
myMap f xs              = [f x | x <- xs]

-- myMap f []           = []
-- myMap f (x:xs)       = [(f x)] ++  myMap f xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f xs           = [x | x <- xs, f x]

-- myFilter f []        = []
-- myFilter f (x:xs)
--  | f x               = x : myFilter f xs
--  | otherwise         = myFilter f xs


-- myAll :: (a -> Bool) -> [a] -> Bool
-- myAll f xs           =    


-- myAny :: (a -> Bool) -> [a] -> Bool

myZip :: [a] -> [b] -> [(a, b)]
myZip xs ys             = [(x,y) | x <- xs, y <- ys]

-- myZip [] _           = []
-- myZip _ []           = []
-- myZip (x:xs) (y:ys)  = [(x,y)] ++ myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = [f x y | (x,y) <- zip xs ys]

-- myZipWith f _ []     = []
-- MyZipWith f [] _     = []
-- MyZipWith f x y      = myMap (uncurry f) (myZip x y)

