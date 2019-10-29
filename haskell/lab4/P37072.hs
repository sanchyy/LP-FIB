data Tree a = Node a (Tree a) (Tree a) | Empty 
    deriving (Show)

size :: Tree a -> Int
size Empty                              = 0
size (Node  _ left_child right_child)   = 1 + size left_child + size right_child

height :: Tree a -> Int
height Empty = 0
height (Node _ left_child right_child)  = 1 + max (height left_child) (height right_child)

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty                       = True
equal _ Empty                           = False
equal Empty _                           = False
equal (Node x l_a r_a) (Node y l_b r_b) 
  | x /= y                              = False
  | otherwise                           = equal l_a l_b && equal r_a r_b

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty                  = True
isomorphic Empty _                      = False
isomorphic _ Empty                      = False
isomorphic (Node x l_a r_a) (Node y l_b r_b) 
  | x /= y                              = False
  | otherwise                           = (isomorphic l_a l_b && isomorphic r_a r_b) || (isomorphic l_a r_b && isomorphic r_a l_b)

preOrder :: Tree a -> [a]
preOrder Empty                          = []
preOrder (Node x l_a r_a)               = [x] ++ preOrder (l_a) ++  preOrder (r_a)

postOrder :: Tree a -> [a]
postOrder Empty                         = []
postOrder (Node x l_a r_a)              = postOrder (l_a) ++  postOrder (r_a) ++ [x]

inOrder :: Tree a -> [a]
inOrder Empty                           = []
inOrder (Node x l_a r_a)                = inOrder (l_a) ++ [x] ++ inOrder (r_a)

bfs [] = []
bfs (Empty:xs) = bfs xs
bfs ((Node x l r):xs) = x : (bfs $ xs ++ [l,r])

breadthFirst :: Tree a -> [a]
breadthFirst t = bfs [t]

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build [x] [y] = Node x Empty Empty
build (h:pre) ind = Node h (build lpre lin) (build rpre rin)
    where
        lin = takeWhile (/= h) ind
        lastl = last lin
        rin = tail $ dropWhile (/= h) ind
        lpre = takeWhile (/= lastl) pre ++ [lastl]
        rpre = tail $ dropWhile (/= lastl) pre


overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ Empty Empty = Empty
overlap _ a Empty = a
overlap _ Empty b = b
overlap f (Node ax al ar) (Node bx bl br) = Node (f ax bx) (overlap f al bl) (overlap f ar br)
