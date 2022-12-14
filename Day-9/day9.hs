import Data.List 

type Coordinate = (Int, Int)

main = do  
        fileData <- parseFile <$> readFile "input.txt"
        let partA = solveInput (replicate 2 (0, 0)) $ fileData
        let partB = solveInput (replicate 10 (0, 0)) $ fileData
        print $ "Solution to part 1: " ++ show partA
        print $ "Solution to part 2: " ++ show partB

parseFile :: String -> [Coordinate]
parseFile = concatMap ((\[dir, steps] -> replicate (read steps) $ directions dir) . words) . lines

directions :: String -> Coordinate
directions "L" = (-1, 0)
directions "R" = (1, 0)
directions "U" = (0, 1)
directions "D" = (0, -1)

evalMove :: Coordinate -> Coordinate -> Coordinate
evalMove (x1, y1) (x2, y2) | (dx, dy) == (2, 2) = (ddx, ddy)
                           | dx == 2            = (ddx, y1)
                           | dy == 2            = (x1, ddy)
                           | otherwise          = (x2, y2)
                           where
                                (dx, dy) = (abs (x1 - x2), abs (y1 - y2))
                                ddx = if x1 > x2 then x1 - 1 else x1 + 1
                                ddy = if y1 > y2 then y1 - 1 else y1 + 1


moveDir :: [Coordinate] -> Coordinate -> [Coordinate]
moveDir xs (dy, dx) = foldl (\nk p -> nk ++ [evalMove (last nk) p]) [(nhx, nhy)] xy
                        where 
                             (hx, hy):xy = xs
                             (nhx, nhy) = (hx + dx, hy + dy)

solveInput :: [Coordinate] -> [Coordinate] -> Int 
solveInput start steps = length . nub . map last . scanl moveDir start $ steps