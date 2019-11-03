multEq :: Int -> Int -> [Int]
multEq x y = iterate (*n) 1
    where
        n =  x*y

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
selectFirst xs ys zs = [x | x <- xs, (belongs x ys) && ((not $ belongs x zs) || ((position x ys) < (position x zs)))]
    where
        belongs :: Int -> [Int] -> Bool
        belongs x [] = False
        belongs x (y:ys) = (x == y) || belongs x ys

        position :: Int -> [Int] -> Int
        position x ys = pos x ys 0
            where
                pos :: Int -> [Int] -> Int -> Int
                pos x (y:ys) it
                  | x == y = it
                  | otherwise = pos x ys (it+1)

myIterate :: (a -> a) -> a -> [a]
myIterate f n = scanl (\x _ -> f x)  n [1..]

SymTab a = String -> Maybe a

empty :: SymTab a
empty   = Nothing 

get :: SymTab a -> String -> Maybe a
get     = ($)

set :: SymTab a -> String -> a -> SymTab 
set taula clau valor c
  | clau == c = Just valor
  | otherwise = taula c

 data Expr a
     = Val a
     | Var String
     | Sum (Expr a) (Expr a)
     | Sub (Expr a) (Expr a)
     | Mul (Expr a) (Expr a)
     deriving Show

eval :: (Num a) => SymTabv a -> Expr a -> Maybe a
