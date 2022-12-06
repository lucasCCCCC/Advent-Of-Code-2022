import Data.List

main = do
    fileData <- readFile "input.txt"
    let partA = messageDetection fileData 4 0
    let partB = messageDetection fileData 14 0
    print $ "Solution to part 1: " ++ show partA
    print $ "Solution to part 2: " ++ show partB


messageDetection :: String -> Int -> Int -> Int 
messageDetection dataStream size index | (length . nub) (take size dataStream) == size = index + size
                                       | otherwise = messageDetection (tail dataStream) size (index + 1)
