eval1 :: String -> Int
eval1 str                               = head $ res (words str) []
    where
        res :: [String] -> [Int] -> [Int]
        res [] stack                    = stack 
        res ("+":next) (x1:x2:stack)    = res next ((x2 + x1) : stack)
        res ("-":next) (x1:x2:stack)    = res next ((x2 - x1) : stack)
        res ("*":next) (x1:x2:stack)    = res next ((x2 * x1) : stack)
        res ("/":next) (x1:x2:stack)    = res next ((div x2 x1) : stack)
        res (n:next)   (stack)          = res next (read(n):stack)

eval2 :: String -> Int
eval2 str                               = head $ foldl res [] $ words str
    where
        res :: [Int] -> String -> [Int]
        res (x1:x2:next) "+"            = (x2+x1):next
        res (x1:x2:next) "-"            = (x2-x1):next
        res (x1:x2:next) "*"            = (x2*x1):next
        res (x1:x2:next) "/"            = (div x2 x1):next
        res next x                      = (read x):next

fsmap :: a -> [a->a] -> a
fsmap x fs                              = foldl $ (flip ($)) x fs

divideNconquer :: (a -> Maybe b) -> (a -> (a, a)) -> (a -> (a, a) -> (b, b) -> b) -> a -> b
divideNconquer base divide conquer x
  | isTrivial $ base x                  = extract $ base x
  | otherwise                           = conquer x (l,r) (ls,rs)
    where
        isTrivial :: Maybe c -> Bool
        isTrivial Nothing               = False
        isTrivial _                     = True

        extract :: Maybe c -> c
        extract (Just z)                = z

        (l,r)                           = divide x
        ls                              = divideNconquer base divide conquer l
        rs                              = divideNconquer base divide conquer r
