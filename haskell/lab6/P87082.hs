main                    = do
    line <- getLine
    if line /= "*"  then do
        putStrLn $ bmi_sol line
        main
    else 
        return ()

bmi_sol :: String -> String
bmi_sol line            = name ++ ": " ++ sol
    where 
        (name, w, h)    = parse line
        sol             = interpret $ bmi w h

parse :: String -> (String, Float, Float)
parse line              = (n,w,h)
    where 
        [n, _w, _h]     = words line
        w               = read _w
        h               = read _h

bmi :: Float -> Float -> Float
bmi m h                 = m / (h*h)

interpret :: Float -> String
interpret x
  | x < 18              = "underweight"  
  | x < 25              = "normal weight" 
  | x < 30              = "overweight"
  | x < 40              = "obese"
  | otherwise           = "severely obese"

