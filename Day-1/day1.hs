import Data.List
import Data.List.Split

main = do
    calories <- reverse . sort . readCalories <$> readFile "input.txt"
    print $ "Solution to part 1: " ++ show (head calories)
    print $ "Solution to part 2: " ++ show (sum $ take 3 calories)

readCalories :: String -> [Int]
readCalories = map (sum . map read . lines) . splitOn "\n\n"