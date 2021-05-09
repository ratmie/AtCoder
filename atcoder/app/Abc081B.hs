module Main where

-- 2で何回割れるかをカウントする関数
countTimesDivBy2 :: Int -> Int
countTimesDivBy2 x
  | x `mod` 2 == 0 = 1 + countTimesDivBy2 (x `div` 2)
  | otherwise = 0

main :: IO ()
main = do
  _ <- getLine -- いらん
  a <- map read . words <$> getLine
  print $ minimum $ map countTimesDivBy2 a

-- n = readLn
-- a = map read . word <$> getLine
-- listにmapでdiv2する、イテレーターにカウントする？