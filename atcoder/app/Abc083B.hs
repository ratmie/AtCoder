module Main where

-- ABC083B - Some Sums

main :: IO ()
main = do
  [n, a, b] <- map read . words <$> getLine
  print $ sum (filter (\x -> (a <= f x) && (f x <= b)) [1 .. n])

--各桁の和を求める
f :: Int -> Int
f 0 = 0
f x = x `mod` 10 + f (x `div` 10)

-- 別解
-- main = do
--  [n, a, b] <- map read . words <$> getLine
--  print $ sum [k | k <- [1..n], evaluate k >= a, evaluate k <= b]

-- evaluate k = sum [read [c] | c <- show k]