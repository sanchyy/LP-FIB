main :: IO()
main                                    = do
    nom <- getLine
    putStrLn $ salutacio nom

salutacio :: String -> String
salutacio nom 
  | head nom == 'A' || head nom == 'a'  = "Hello!"
  | otherwise                           = "Bye!"

