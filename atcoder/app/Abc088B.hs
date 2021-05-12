module Main where

import Data.List (sort)

main :: IO ()
main = do
  getLine
  a <- map read . words <$> getLine
  print $ sum $ zipWith (*) (cycle [1, -1]) $ reverse $ sort a

-- ソートして、２つに分けて、sumとって引き算
