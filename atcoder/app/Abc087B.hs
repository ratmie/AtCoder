module Main where

main :: IO ()
main = do
  a <- readLn :: IO Int
  b <- readLn :: IO Int
  c <- readLn :: IO Int
  x <- readLn :: IO Int
  print $ length [() | u <- [0 .. a], v <- [0 .. b], y <- [0 .. c], 500 * u + 100 * v + 50 * y == x]
