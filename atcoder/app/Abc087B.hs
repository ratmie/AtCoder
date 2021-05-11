module Main where

main :: IO ()
main = do
  a <- readLn :: IO Int
  b <- readLn :: IO Int
  c <- readLn :: IO Int
  x <- readLn :: IO Int
  print $ length [aa | aa <- [0 .. a], bb <- [0 .. b], cc <- [0 .. c], 500 * aa + 100 * bb + 50 * cc == x]
