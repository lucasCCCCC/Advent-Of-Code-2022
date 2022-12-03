import Data.List
import Data.Char

main = do 
        fileData <- readFile "input.txt"
        let a = findDuplicate $ map splitString $ lines fileData
        let b = findDuplicateIn3 $ lines fileData
        print $ "Solution to part 1: " ++ show a
        print $ "Solution to part 2: " ++ show b

splitString :: String -> (String, String)
splitString s = splitAt (div (length s + 1) 2) s 

findDuplicate :: [(String, String)] -> Int 
findDuplicate []          = 0
findDuplicate ((x, y):xs) = getPriority (head $ intersect x y) + findDuplicate xs

findDuplicateIn3 :: [String] -> Int 
findDuplicateIn3 []                 = 0 
findDuplicateIn3 xs | length xs < 3 = 0
findDuplicateIn3 (x:y:z:zs)         = (getPriority $ head $ intersect z $ intersect x y) + findDuplicateIn3 zs 

getPriority :: Char -> Int 
getPriority c = ord c - (if isUpper c then 38 else 96)

