module Main where

main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine
  -- 関数化しないとパターンマッチできないからif文にしている？
  if (a * b) `mod` 2 == 0 then putStrLn "Even" else putStrLn "Odd"

--   putStrLn $ isEvenProduct a b

-- isEvenProduct :: Integer -> Integer -> String
-- isEvenProduct a b
--   | even (a * b) = "Even"
--   | otherwise = "Odd"