module Main where

main :: IO ()
main = do
  a <- readLn :: IO Int
  [b, c] <- map read . words <$> getLine
  s <- getLine
  putStrLn $ unwords [show (a + b + c), s]
