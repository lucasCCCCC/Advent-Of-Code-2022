main = do
    fileData <- readFile "input.txt"
    let plays = map play (lines fileData)
                where play s = let (s1:s2:[]) = words s in (s1 !! 0, s2 !! 0)

    print $ "Solution to part 1: " ++ show (sum $ map gameOutcomeScores1 plays)
    print $ "Solution to part 2: " ++ show (sum $ map gameOutcomeScores2 plays)

gameOutcomeScores1 :: (Char, Char) -> Int
gameOutcomeScores1 ('A','X') = 4
gameOutcomeScores1 ('B','Y') = 5
gameOutcomeScores1 ('C','Z') = 6
gameOutcomeScores1 ('B','X') = 1
gameOutcomeScores1 ('C','X') = 7
gameOutcomeScores1 ('A','Y') = 8
gameOutcomeScores1 ('C','Y') = 2
gameOutcomeScores1 ('A','Z') = 3
gameOutcomeScores1 ('B','Z') = 9

gameOutcomeScores2 :: (Char, Char) -> Int
gameOutcomeScores2 ('A','X') = 3
gameOutcomeScores2 ('B','Y') = 5
gameOutcomeScores2 ('C','Z') = 7
gameOutcomeScores2 ('B','X') = 1
gameOutcomeScores2 ('C','X') = 2
gameOutcomeScores2 ('A','Y') = 4
gameOutcomeScores2 ('C','Y') = 6
gameOutcomeScores2 ('A','Z') = 8
gameOutcomeScores2 ('B','Z') = 9