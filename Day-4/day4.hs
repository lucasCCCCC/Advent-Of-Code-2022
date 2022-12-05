import Data.List 

main = do 
        fileData <- readFile "input.txt"
        let assignments = lines fileData
        let parsedAssignments = map (stringToInteger . (\(a,b) -> (splitListAt '-' a, splitListAt '-' b)) . (splitListAt ',')) assignments
        let partA = sum $ map (fromEnum . assignmentContains) parsedAssignments
        let partB = sum $ map (fromEnum . assignmentOverlaps) parsedAssignments
        print $ "Solution to part 1: " ++ show partA
        print $ "Solution to part 2: " ++ show partB

stringToInteger :: ((String, String), (String, String)) -> ((Int, Int), (Int, Int))
stringToInteger ((a, b), (x, y)) = ((read a :: Int, read b :: Int), (read x :: Int, read y :: Int))

splitListAt :: (Eq a) => a -> [a] -> ([a], [a])
splitListAt n xs = (\(x, y) -> (x, drop 1 y)) $ break (== n) xs 

assignmentOverlaps :: (Ord a) => ((a, a), (a, a)) -> Bool 
assignmentOverlaps ((a, b), (x, y)) = (a <= x && b >= x) || (x <= a && y >= a)

assignmentContains :: (Ord a) => ((a, a), (a, a)) -> Bool 
assignmentContains ((a, b), (x, y)) = (a >= x && b <= y) || (x >= a && y <= b)