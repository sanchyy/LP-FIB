data Queue a = Queue [a] [a]
     deriving (Show)

create :: Queue a
create                                  = Queue [] []

push :: a -> Queue a -> Queue a
push n  (Queue x y)                     = Queue x (n:y)

pop :: Queue a -> Queue a
pop (Queue [] [])                       = Queue [] [] 
pop (Queue [] y)                        = Queue (tail $ reverse y) []
pop (Queue x y)                         = Queue (tail x) y

top :: Queue a -> a
top (Queue [] y)                        = head $ reverse y
top (Queue x y)                         = head x  

empty :: Queue a -> Bool
empty (Queue [] [])                     = True
empty _                                 = False

instance Eq a => Eq (Queue a)
    where
        (Queue x1 y1) == (Queue x2 y2)  = x1 ++ reverse y1 == x2 ++ reverse y2

instance Functor (Queue) 
    where
        fmap f (Queue x y)              = (Queue (map f x) (map f y))

translation :: Num b => b -> Queue b -> Queue b
translation t                           = fmap (+t) 

-- (<*>) :: f (a -> b) -> (f a -> f b)
instance Applicative Queue
    where
        (Queue [x] []) <*> q            = (Queue [] [x]) <*> q
        (Queue [] [x]) <*> q            = (Queue [x] []) <*> q
        pure x                          = (Queue [x] [])

merge :: Queue a -> Queue a -> Queue a
merge (Queue x1 y1) (Queue x2 y2)       = Queue (x1 ++ reverse y1) (x2 ++ reverse y2)


-- return :: a -> m a
-- (>>=)  :: m a -> (a -> m b) -> m b
-- (>>)   :: m a -> m b -> m b
instance Monad Queue 
    where
        return x                        = Queue [x] []
        (Queue x y) >>= f               = foldl merge create (map f (x ++ (reverse y)))  

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter f q = do
    v <- q
    if f v then return v else create


