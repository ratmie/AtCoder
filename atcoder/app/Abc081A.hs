module Main where

main :: IO ()
main = getLine >>= print . length . filter (== '1')

-- 以下と同じ意味
-- s <- getLine
-- print . length . filter (== '1') $ s

-- 入力が 1 0 1 だと思っていたが101だった
-- s <- map read . words <$> getLine
-- putStrLn $ show (sum s)

-- 文字列を数字のリストに変換して集計するつもりだったけれど、文字のママfilterして長さを数えるのはスマートで感動する
