module Main where

import Control.Monad (replicateM)
import Data.List (group, sort)

main :: IO ()
main = do
  -- 縦の読み込み
  n <- readLn
  ds <- replicateM n readLn
  -- groupは隣り合っている重複を取り除くので先にソート
  print $ length $ group $ sort (ds :: [Integer])

-- 重複を取り除いてsortする？
