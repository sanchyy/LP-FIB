exps :: Float -> [Float]
exps n          = zipWith (/) pow fact
    where 
        fact    = scanl (*) 1 $ iterate (+1) 1
        pow     = [n ** i | i <- [1..]]

exponencial :: Float -> Float -> Float
exponencial x e = sum $ takeWhile (>= e) $ exps x 

