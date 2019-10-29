exps :: Float -> [Float]
exps n          = zipWith (/) pow fact
    where 
        fact    = scanl (*)  1 $ iterate (+1) 1
        pow     = iterate (*n) 1.0 

exponencial :: Float -> Float -> Float
exponencial x e = sum $ takeWhile (>= e) $ exps x 

