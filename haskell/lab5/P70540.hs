data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1 :: Expr -> Int
eval1 (Val x)       = x
eval1 (Add x y)     = eval1 x + eval1 y
eval1 (Sub x y)     = eval1 x - eval1 y
eval1 (Mul x y)     = eval1 x * eval1 y
eval1 (Div x y)     = eval1 x `div` eval1 y



